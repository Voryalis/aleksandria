# Aleksandria — From Data to Learning

An English-language Python learning game for university beginners studying Big Data and Connectionist AI.

## Run

Requires Python 3.9 or newer. No pip packages, account, or internet connection are needed.

1. Extract the ZIP.
2. Open a terminal in the extracted folder.
3. Run `python3 game.py` on macOS/Linux, or `py game.py` on Windows.
4. The game opens in your browser. If it does not, copy the local URL printed in the terminal into your browser.
5. Keep the terminal running while playing. Press Ctrl+C to stop it.

On Windows you can also double-click `Start-Windows.bat`. On macOS, `Start-Mac.command` is provided; if macOS refuses to open it, use the terminal command above.

The server listens only on your own computer (127.0.0.1), with an automatically selected available port. It is a local teaching tool, not a public web service.

## Gameplay

- Mission 1: remove training/test overlap, separate labels, normalize pixels.
- Mission 2: interpret a mistaken digit prediction and order the learning steps.
- Mission 3: adjust the learning rate and run real gradient-descent updates.
- Mission 4: reason about generalization, data representativeness, and human oversight.

Seven questions award one point each on the first correct attempt. Wrong answers show explanations and permit retries. Completing the neuron challenge awards three points. Maximum: 10. At the end, download a plain-text learning summary or replay.

## What is actually calculated?

Python calculates a single sigmoid neuron with one synthetic input x = 1 and target y = 1:

- z = w × x + b
- p = sigmoid(z)
- L = −log(p), binary cross-entropy for y = 1
- dL/dw = (p − y) × x
- dL/db = p − y
- parameter_new = parameter_old − learning_rate × gradient

Start: w = −1, b = 0. Goal: loss below 0.30. Both parameters are updated using the same pre-update gradients. The permitted learning rates are 0.1–1.0.

This deliberately small challenge demonstrates parameter updates. It does not train on MNIST, recognize uploaded digits, implement a multilayer network, or establish test-set accuracy. The digit scores in Mission 2 are illustrative. A lower training loss is not proof of generalization.

## Verification

Run `python3 -m unittest -v test_game.py` (Windows: `py -m unittest -v test_game.py`).

Checks performed:

- Gradient agrees with a numerical finite-difference calculation.
- The training goal is reachable at every slider setting, with decreasing loss in this example.
- HTTP handlers serve the game, score all question answers, calculate updates, and reject invalid learning rates. This is tested with in-memory requests.

The development environment blocked opening a local server port, so a complete browser playthrough remains pending. Before submission, play all four missions on your computer and ask another teammate to try the game. Record actual feedback and any corrections in the QA log. Downloaded summaries are not a substitute for an independent learner trial.

## Repository location

This game lives at `interactive-learning/python-game/` in the Aleksandria repository. It is an optional interactive supplement, not a replacement for the Study Guide or Test Bank.

## AI-use disclosure

This initial implementation and its tests were generated with AI assistance at the Quality Lead's request. Team review, adaptation, and the independent learner trial should be documented before submission. Do not describe this initial version as independently tested by a teammate until that has happened.
