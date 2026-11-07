#!/usr/bin/env python3
"""Aleksandria Learning Lab. Python 3.9+, standard library only."""
import argparse
import json
import math
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

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

HTML = r'''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Aleksandria · Learning Lab</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f3f7fb;color:#143047;font:17px system-ui,sans-serif}header{background:#143047;color:white;padding:28px max(6vw,20px)}header small{color:#84e3db;letter-spacing:2px}h1{font-size:clamp(26px,5vw,40px);margin:10px 0}header p{margin:6px 0;color:#d0dce7}main{max-width:940px;margin:24px auto;padding:0 18px}.bar{height:9px;background:#dce6ee;border-radius:9px;overflow:hidden}.bar div{height:100%;background:#009f95;transition:width .4s}.status{display:flex;justify-content:space-between;margin:14px 0;color:#4a6175;font-size:14px}.card{background:white;padding:clamp(20px,4vw,36px);border:1px solid #dbe5ef;border-radius:20px;box-shadow:0 12px 35px #1530490a}h2{font-size:25px;margin-top:0}p{line-height:1.6}button{font:inherit;cursor:pointer;border:0;border-radius:10px;padding:14px 20px;background:#143047;color:white;margin:5px 0}button:hover{filter:brightness(1.15)}button:focus-visible,input:focus-visible{outline:3px solid #ebaa29;outline-offset:3px}button:disabled{opacity:.55;cursor:default}.choice{display:block;width:100%;text-align:left;background:#edf4fa;color:#143047;border:2px solid transparent;margin:10px 0}.choice.correct{border-color:#008670;background:#e2f5ee}.choice.wrong{border-color:#bd493f;background:#fff0ec}.feedback{padding:16px;background:#eaf5f5;border-left:4px solid #00887f;margin-top:18px;line-height:1.6}.muted{color:#597185;font-size:14px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.metric{background:#f2f6fa;padding:16px;border-radius:12px}.metric b{display:block;font-size:25px;margin-top:9px}.flow{display:flex;align-items:center;justify-content:space-around;gap:10px;margin:24px 0}.node{padding:20px;background:#e8f7f5;border:2px solid #00998c;border-radius:16px;text-align:center}.track{height:18px;background:#e5ebf1;border-radius:10px;margin:12px 0;overflow:hidden}.fill{height:100%;background:#009f95;transition:width .4s}label{display:block;margin-top:20px}input{width:100%;accent-color:#008d83}footer{text-align:center;padding:20px;font-size:13px;color:#5a7080}ul{line-height:1.8}#error{color:#ae2929}.badge{color:#00796e;font-weight:700}@media(max-width:550px){.grid{grid-template-columns:1fr}.flow{font-size:13px}.node{padding:12px}}
</style>
<header><small>TEAM ALEKSANDRIA / INTERACTIVE LEARNING</small><h1>From Data to Learning</h1><p>Clean the data. Read a prediction. Train a neuron. Test your judgement.</p></header>
<main><div class="bar"><div id="progress" style="width:0%"></div></div><div class="status"><span id="stage">Ready to start</span><span id="score">Score: 0 / 10</span></div><section class="card" id="screen"></section><p id="error" role="alert"></p></main>
<footer>Big Data & Connectionist AI · Educational simulation · No account or internet required</footer>
<script>
let qs=[], index=0,score=0,attempts=0,steps=0,w=-1,b=0,initialLoss=0,finished=false;
const $=id=>document.getElementById(id);
async function api(path,body){const response=await fetch(path,{method:body?'POST':'GET',headers:{'Content-Type':'application/json'},body:body?JSON.stringify(body):undefined});if(!response.ok)throw new Error('Request failed. Keep the Python program running and try again.');return response.json()}
function update(n){$('progress').style.width=(n/8*100)+'%';$('score').textContent='Score: '+score+' / 10'}
function intro(){$('screen').innerHTML=`<span class="badge">4 MISSIONS · ABOUT 5–8 MINUTES</span><h2>Can you help a model learn?</h2><p>Your mission is to prepare handwriting data and understand why a prediction can be wrong. You will then run real gradient-descent updates on one tiny neuron.</p><ul><li>Seven questions: one point for each first-try correct answer.</li><li>Neuron challenge: three points for lowering the loss below 0.30.</li><li>Incorrect answers have feedback and can be retried.</li></ul><p class="muted">The neuron challenge uses one synthetic input and label. It is not an MNIST classifier and does not demonstrate test accuracy.</p><button id="start">Start the lab →</button>`;$('start').onclick=question}
function question(){attempts=0;update(index<5?index:index+1);const q=qs[index];$('stage').textContent=q.title;$('screen').innerHTML='<h2>'+q.title+'</h2><p>'+q.question+'</p><div id="choices"></div><div id="feedback" aria-live="polite"></div>';q.options.forEach((v,i)=>{let btn=document.createElement('button');btn.className='choice';btn.textContent=String.fromCharCode(65+i)+'. '+v;btn.onclick=()=>answer(i,btn);$('choices').appendChild(btn)})}
async function answer(option,btn){try{const result=await api('/answer',{question:index,option});attempts++;if(!result.correct){btn.classList.add('wrong');btn.disabled=true;$('feedback').innerHTML='<div class="feedback"><b>Try again.</b> '+result.explanation+'</div>';return}if(attempts===1)score++;btn.classList.add('correct');document.querySelectorAll('.choice').forEach(x=>x.disabled=true);$('feedback').innerHTML='<div class="feedback"><b>Correct.</b> '+result.explanation+'</div><button id="next">Continue →</button>';$('next').onclick=()=>{index++;if(index===5)training();else if(index===qs.length)end();else question()};$('score').textContent='Score: '+score+' / 10'}catch(e){$('error').textContent=e.message}}
async function training(){try{update(5);$('stage').textContent='Mission 3 · Train one neuron';let n=await api('/neuron',{weight:w,bias:b});initialLoss=n.loss;$('screen').innerHTML=`<h2>Turn an error into an update</h2><p>For this synthetic example, <b>input x = 1</b> and the separate <b>target y = 1</b>. The neuron computes <b>p = sigmoid(w × x + b)</b>. Lower binary cross-entropy loss means a better match to this one target.</p><div class="flow"><div class="node">Input<br><b>x = 1</b></div><span>→</span><div class="node">Sigmoid neuron<br><b>w × x + b</b></div><span>→</span><div class="node">Output<br><b id="output"></b></div></div><div class="grid"><div class="metric">Loss<b id="loss"></b></div><div class="metric">Weight<b id="weight"></b></div><div class="metric">Bias<b id="bias"></b></div></div><div class="track"><div class="fill" id="confidence"></div></div><label for="rate">Learning rate: <b id="rateLabel">0.50</b></label><input id="rate" type="range" min="0.1" max="1" step="0.1" value="0.5"><p class="muted">Here, dL/dw = (p − y) × x and dL/db = p − y. Each update subtracts learning rate × gradient. Our slider is limited to 0.1–1.0; other problems and larger steps may behave differently.</p><button id="train">Run one training step</button> <button id="reset">Reset neuron</button><div id="trainFeedback" aria-live="polite"></div><div id="continue"></div>`;$('rate').oninput=()=>{$('rateLabel').textContent=Number($('rate').value).toFixed(2)};$('train').onclick=step;$('reset').onclick=()=>{w=-1;b=0;steps=0;training()};paint(n)}catch(e){$('error').textContent=e.message}}
function paint(n){$('output').textContent=n.prediction.toFixed(3);$('loss').textContent=n.loss.toFixed(4);$('weight').textContent=n.weight.toFixed(3);$('bias').textContent=n.bias.toFixed(3);$('confidence').style.width=n.prediction*100+'%'}
async function step(){const button=$('train');button.disabled=true;try{let n=await api('/step',{weight:w,bias:b,rate:Number($('rate').value)});w=n.weight;b=n.bias;steps++;paint(n);$('trainFeedback').innerHTML='<div class="feedback"><b>Step '+steps+'</b> · Loss changed from '+n.previous_loss.toFixed(4)+' to '+n.loss.toFixed(4)+'.<br>The optimizer updated both weight and bias. This result applies to our single training example.</div>';if(n.loss<.30){$('continue').innerHTML='<p class="badge">Challenge completed! Loss is below 0.30.</p><button id="next">Collect 3 points and continue →</button>';$('next').onclick=()=>{score+=3;question()};$('reset').disabled=true}else button.disabled=false}catch(e){$('error').textContent=e.message;button.disabled=false}}
function end(){finished=true;update(8);$('stage').textContent='Lab complete';$('screen').innerHTML=`<span class="badge">MISSION COMPLETE</span><h2>Your score: ${score} / 10</h2><p>You prepared inputs, separated labels from predictions, and ran ${steps} real gradient-descent updates.</p><ul><li>Good data includes quality, not just quantity.</li><li>Backpropagation computes gradients; optimizers update parameters.</li><li>Training loss is not proof of performance on unseen data.</li></ul><p class="muted">This score measures your performance in this learning game. It is not model accuracy. No personal data or results are saved.</p><button id="replay">Play again</button> <button id="save">Save learning summary</button>`;$('replay').onclick=()=>location.reload();$('save').onclick=()=>{let t=`Aleksandria Learning Lab\nCompleted: ${new Date().toLocaleString()}\nQuiz first-try score: ${score-3}/7\nNeuron challenge: 3/3\nTraining steps: ${steps}\nTotal: ${score}/10\nThis is a local game summary, not evidence of independent teammate review.\n`;let a=document.createElement('a');a.href=URL.createObjectURL(new Blob([t],{type:'text/plain'}));a.download='aleksandria-learning-summary.txt';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)}}
api('/questions').then(data=>{qs=data;intro()}).catch(e=>{$('error').textContent=e.message});
</script></html>'''

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def send(self, payload, status=200, html=False):
        data = payload.encode('utf-8') if html else json.dumps(payload).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'text/html; charset=utf-8' if html else 'application/json')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == '/':
            self.send(HTML, html=True)
        elif self.path == '/questions':
            self.send([{k: q[k] for k in ('title', 'question', 'options')} for q in QUESTIONS])
        else:
            self.send({'error': 'Not found'}, 404)

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
    print('Aleksandria Learning Lab is running at ' + url, flush=True)
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
