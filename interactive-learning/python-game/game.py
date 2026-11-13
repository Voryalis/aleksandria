#!/usr/bin/env python3
"""Operation World Line - Aleksandria Learning Lab. Python 3.9+, standard library only."""
import argparse
import json
import math
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

WEB_DIR = Path(__file__).resolve().with_name('web')
CONTENT_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'text/javascript; charset=utf-8',
    '.webp': 'image/webp',
    '.woff2': 'font/woff2',
}
WEB_FILES = {
    '/': WEB_DIR / 'index.html',
    '/game.css': WEB_DIR / 'game.css',
    '/game.js': WEB_DIR / 'game.js',
    **{
        f'/assets/{asset.name}': asset
        for asset in (WEB_DIR / 'assets').iterdir()
        if asset.is_file() and asset.suffix in ('.webp', '.woff2')
    },
}

QUESTIONS = [
    dict(title='Mission 1 · Clean the dataset', question='You find the same handwritten image in both training and test data. What should you do?', options=['Keep both: more data is always better.', 'Remove the overlap before evaluating the model.', 'Copy all training images into the test set.'], answer=1, explanation='Overlap can leak training information into evaluation and inflate the score. Keep test examples separate; when possible, split by writer too.'),
    dict(title='Mission 1 · Keep the label separate', question='An image shows the digit 5. Which item belongs in the input?', options=['The correct answer 5, so the model can copy it.', 'Only the name of the person who wrote it.', 'Pixel values; keep label 5 as the training target.'], answer=2, explanation='The model receives pixel features. During supervised training, its prediction is compared with the separate correct label.'),
    dict(title='Mission 1 · Prepare pixels', question='For an 8-bit grayscale pixel of value 128, what is x / 255 approximately?', options=['0.502', '128.0', '255.0'], answer=0, explanation='128 / 255 is approximately 0.502. Dividing by 255 scales this 0–255 pixel representation to 0–1. Apply the same preprocessing at prediction time.'),
    dict(title='Mission 2 · Read a prediction', question='For an image labelled 5, a model gives scores: digit 3 = 0.60, digit 5 = 0.30, all other digits combined = 0.10. What is its prediction?', options=['5, because that is the label.', '3, because it has the largest individual score.', 'The model has no prediction.'], answer=1, explanation='The predicted class is 3, while the correct training label is 5. A probability-like score is a model output, not a guarantee of correctness. These values are illustrative.'),
    dict(title='Mission 2 · Follow the training cycle', question='What comes after computing the loss?', options=['Backpropagation computes gradients; an optimizer updates parameters.', 'The correct answer is permanently stored in every neuron.', 'The test labels become input pixels.'], answer=0, explanation='Backpropagation computes gradients of the loss. The optimizer uses those gradients to update parameters. They are related but distinct steps.'),
    dict(title='Mission 4 · Test what was learned', question='Your training loss became smaller. Does this prove the network works on unseen handwriting?', options=['Yes, a smaller training loss proves perfect accuracy.', 'No. Evaluate on held-out examples not used for updates.', 'Yes, if you use the training images again.'], answer=1, explanation='Training progress alone does not prove generalization. Evaluate on held-out data; keep a final test set separate from model selection.'),
    dict(title='Mission 4 · Responsible AI', question='A handwriting system performs poorly for some writers. What is the best next step?', options=['Hide those mistakes from the report.', 'Claim the system is equally reliable for everyone.', 'Investigate representative data and subgroup errors, and allow human review.'], answer=2, explanation='Data quantity alone is not enough. Quality and representativeness matter. Report limitations and use human oversight where mistakes have consequences.')
]

def neuron(weight, bias):
    """One actual sigmoid neuron; x=1, y=1, binary cross-entropy."""
    z = weight + bias
    p = 1.0 / (1.0 + math.exp(-z))
    loss = max(z, 0) - z + math.log1p(math.exp(-abs(z)))
    return dict(weight=weight, bias=bias, z=z, prediction=p, loss=loss, gradient=p-1)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def send(self, payload, status=200):
        self.send_bytes(json.dumps(payload).encode('utf-8'), 'application/json', status)

    def send_bytes(self, data, content_type, status=200):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = self.path.partition('?')[0]
        if path == '/questions':
            self.send([{k: q[k] for k in ('title', 'question', 'options')} for q in QUESTIONS])
            return
        file = WEB_FILES.get(path)
        if file is None:
            self.send({'error': 'Not found'}, 404)
            return
        try:
            data = file.read_bytes()
        except FileNotFoundError:
            self.send({'error': 'Not found'}, 404)
            return
        self.send_bytes(data, CONTENT_TYPES[file.suffix])

    def do_POST(self):
        try:
            size = int(self.headers.get('Content-Length', 0))
            if not 0 < size <= 4096:
                raise ValueError('Invalid request size')
            data = json.loads(self.rfile.read(size))
            if self.path == '/answer':
                i, option = data['question'], data['option']
                if type(i) is not int or not 0 <= i < len(QUESTIONS):
                    raise ValueError('Invalid question')
                q = QUESTIONS[i]
                if type(option) is not int or not 0 <= option < len(q['options']):
                    raise ValueError('Invalid option')
                self.send(dict(correct=option == q['answer'], explanation=q['explanation']))
            elif self.path in ('/neuron', '/step'):
                w, b = float(data['weight']), float(data['bias'])
                if not all(math.isfinite(v) and abs(v) <= 50 for v in (w, b)):
                    raise ValueError('Parameters out of range')
                old = neuron(w, b)
                if self.path == '/step':
                    rate = float(data['rate'])
                    if not math.isfinite(rate) or not 0.1 <= rate <= 1:
                        raise ValueError('Learning rate out of range')
                    result = neuron(w-rate*old['gradient'], b-rate*old['gradient'])
                    result['previous_loss'] = old['loss']
                    self.send(result)
                else:
                    self.send(old)
            else:
                self.send({'error': 'Not found'}, 404)
        except (KeyError, ValueError, TypeError, OverflowError):
            self.send({'error': 'Invalid request'}, 400)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--no-browser', action='store_true')
    parser.add_argument('--port', type=int, default=0, help='Local port (default: choose an available port)')
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    url = 'http://127.0.0.1:%s' % server.server_port
    print('Operation World Line is running at ' + url, flush=True)
    print('Keep this window open. Press Ctrl+C to stop.', flush=True)
    if not args.no_browser:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__ == '__main__':
    main()
