import json
import math
import threading
import unittest
import urllib.request
import urllib.error
from http.server import ThreadingHTTPServer
from game import Handler, QUESTIONS, neuron

class GameTests(unittest.TestCase):
    def test_gradient_against_finite_difference(self):
        for w, b in [(-1, 0), (0.2, -0.1), (2, 1)]:
            h = 1e-6
            numerical = (neuron(w+h,b)['loss']-neuron(w-h,b)['loss'])/(2*h)
            self.assertAlmostEqual(numerical, neuron(w,b)['gradient'], places=6)

    def test_challenge_reachable_for_every_slider_setting(self):
        for k in range(1, 11):
            w, b = -1, 0
            for step in range(100):
                n = neuron(w,b)
                if n['loss'] < .3:
                    break
                w -= k/10*n['gradient']
                b -= k/10*n['gradient']
                self.assertLess(neuron(w,b)['loss'], n['loss'])
            self.assertLess(neuron(w,b)['loss'], .3)

    def test_http_game_flow(self):
        import io
        class Connection:
            def __init__(self, raw):
                self.raw = raw
                self.output = b''
            def makefile(self, *args):
                return io.BytesIO(self.raw)
            def sendall(self, data):
                self.output += data
        def request(path, data=None):
            body = json.dumps(data).encode() if data is not None else b''
            method = 'POST' if data is not None else 'GET'
            head = f'{method} {path} HTTP/1.0\r\nContent-Length: {len(body)}\r\n\r\n'.encode()
            connection = Connection(head+body)
            Handler(connection, ('127.0.0.1', 1), None)
            headers, payload = connection.output.split(b'\r\n\r\n', 1)
            status = int(headers.split()[1])
            return status, payload
        status, html = request('/')
        self.assertEqual(status, 200)
        self.assertIn(b'From Data to Learning', html)
        status, raw = request('/questions')
        public = json.loads(raw)
        self.assertEqual(len(public), 7)
        self.assertNotIn('answer', public[0])
        for i, q in enumerate(QUESTIONS):
            status, raw = request('/answer', dict(question=i,option=q['answer']))
            self.assertTrue(json.loads(raw)['correct'])
            status, raw = request('/answer', dict(question=i,option=(q['answer']+1)%3))
            self.assertFalse(json.loads(raw)['correct'])
        status, raw = request('/step', dict(weight=-1,bias=0,rate=.5))
        n = json.loads(raw)
        self.assertLess(n['loss'], n['previous_loss'])
        status, raw = request('/step', dict(weight=-1,bias=0,rate=99))
        self.assertEqual(status,400)

if __name__ == '__main__':
    unittest.main()
