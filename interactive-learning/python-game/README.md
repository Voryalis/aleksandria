# Aleksandria — Operation World Line

An English-language Python learning game for university beginners studying Big Data and Connectionist AI. A D-Mail dated tomorrow arrives at the Future Gadget Lab. Read it on Okabe’s phone, then help the lab check a handwriting model before sending a reply.

## Run

Requires Python 3.9 or newer. No pip packages, account, or internet connection are needed.

1. Extract the ZIP or clone the repository.
2. Open a terminal in the `python-game` folder. Keep the bundled `web/` folder beside `game.py`.
3. Run `python3 game.py` on macOS/Linux, or `py game.py` on Windows.
4. The game opens in your browser. If it does not, copy the local URL printed in the terminal into your browser.
5. Keep the terminal running while playing. Press Ctrl+C to stop it.

On Windows you can also double-click `Start-Windows.bat`. On macOS, `Start-Mac.command` is provided; if macOS refuses to open it, use the terminal command above.

The server listens only on your own computer (127.0.0.1), with an automatically selected available port. It is a local teaching tool, not a public web service.

## Gameplay

- **The duplicate.** Remove training/test overlap, separate labels, and normalize pixels.
- **The wrong digit.** Interpret a mistaken digit prediction and order the learning steps.
- **PhoneWave.** Adjust the learning rate and run gradient-descent updates.
- **One last check.** Reason about generalization, data representativeness, and human oversight.

Seven questions award one point each on the first correct attempt. Wrong answers show explanations and permit retries. Completing the neuron challenge awards three points. Maximum: 10. At the end, download a plain-text learning summary or replay.

Use **Backlog** to reread dialogue and **D-Mail** to reopen the phone. The simulated divergence meter follows the story through the eight checks. The score records quiz and neuron challenge results.

## Art and font credits

The artwork retains its original rights and falls outside the repository's MIT and CC BY 4.0 licenses. The Spriters Resource archives the source images below.

- *Steins;Gate (Steam HD Edition)*, archived by Adrot. [Future Gadget Laboratory](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107557/), [Kurisu](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107532/), [Daru](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107534/), [Mayuri](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107547/), [phone](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107517/), and [divergence meter](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107527/).
- *Steins;Gate: Linear Bounded Phenogram*, archived by delta. [Okabe](https://www.spriters-resource.com/pc_computer/steinsgatelinearboundedphenogram/asset/153185/).
- [Instrument Serif license](web/assets/instrument-serif-OFL.txt), [Instrument Sans license](web/assets/instrument-sans-OFL.txt), and [IBM Plex Mono license](web/assets/ibm-plex-OFL.txt).

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
- HTTP handlers serve the game and its sprite assets, score all question answers, calculate updates, and reject invalid learning rates. This is tested with in-memory requests.
- Automated Chromium playthroughs covered all four missions, scoring, reset, replay, and summary downloads at desktop and phone widths.

Before submission, play all four missions on your computer and ask another teammate to try the game. Record feedback and any corrections in the QA log. Downloaded summaries are not a substitute for an independent learner trial.

## Repository location

This game lives at `interactive-learning/python-game/` in the Aleksandria repository. It is an optional interactive supplement, not a replacement for the Study Guide or Test Bank.

## AI-use disclosure

The initial implementation and its tests were generated with AI assistance at the Quality Lead's request. The Operation World Line interface and mission framing also used AI assistance. Team review, adaptation, and the independent learner trial should be documented before submission.
