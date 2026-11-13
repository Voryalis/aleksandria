# Aleksandria — Operation World Line

An English-language Python learning game for university beginners studying Big Data and Connectionist AI. A D-Mail dated tomorrow arrives at the Future Gadget Lab. Read it on Okabe’s phone, then help the lab check a handwriting model before sending a reply.

## Installation

Requires **Python 3.9 or newer** and a current web browser. The server uses Python’s standard library. The included `web/` folder contains the interface, art, and fonts, so the downloaded game works offline.

### Get the files

Download and extract the [repository ZIP](https://github.com/Voryalis/aleksandria/archive/refs/heads/main.zip), then open `aleksandria-main/interactive-learning/python-game/`.

Alternatively, clone the repository with Git and enter the game folder.

```bash
git clone https://github.com/Voryalis/aleksandria.git
cd aleksandria/interactive-learning/python-game
```

For an existing Git checkout, run `git pull` from the repository before launching. When using a ZIP download, extract the complete updated folder so that `game.py` and `web/` come from the same version.

### Windows

Install Python from [python.org](https://www.python.org/downloads/). Open `Start-Windows.bat` in the game folder, or run the following command in PowerShell or Command Prompt from that folder.

```powershell
py -3 game.py
```

The launcher also accepts a Python 3 installation available as `python`.

### macOS

Install Python 3 from [python.org](https://www.python.org/downloads/) if needed. Double-click `Start-Mac.command` in the game folder. You can also open a terminal in that folder and run the following command.

```bash
python3 game.py
```

If a ZIP extraction leaves the launcher without execute permission, run `chmod +x Start-Mac.command` from the game folder, or use the Python command above.

### Linux

Install Python 3 through your distribution’s package manager if needed. Open a terminal in the game folder and run the following command.

```bash
python3 game.py
```

### During play

The game opens in your browser. If it stays closed, copy the local address printed in the terminal. Keep the terminal running during play and press Ctrl+C to stop the game.

The server listens on your own computer at `127.0.0.1` and automatically selects an available port. To select a port or open the browser yourself, run `python3 game.py --port 8000 --no-browser` and visit `http://127.0.0.1:8000`. Use `py -3` in place of `python3` on Windows.

### Troubleshooting

| Symptom | Action |
| --- | --- |
| Python command unavailable or version below 3.9 | Install Python 3.9 or newer, reopen the terminal, and check `python3 --version` on macOS/Linux or `py -3 --version` on Windows |
| Missing interface, artwork, or fonts | Extract or clone the full game folder, including `web/` and `web/assets/` |
| Browser cannot reconnect during play | Keep the Python terminal running and use its printed address |
| A chosen port is already in use | Omit `--port` to let the game choose an available port |

## Gameplay

- **The duplicate.** Remove training/test overlap, separate labels, and normalize pixels.
- **The wrong digit.** Interpret a mistaken digit prediction and order the learning steps.
- **PhoneWave.** Adjust the learning rate and run gradient-descent updates.
- **One last check.** Reason about generalization, data representativeness, and human oversight.

Seven questions award one point each on the first correct attempt. Wrong answers show explanations and permit retries. Completing the neuron challenge awards three points. Maximum: 10. At the end, download a plain-text learning summary or replay.

Use **Backlog** to reread dialogue and **D-Mail** to reopen the phone. The simulated divergence meter follows the story through the eight checks. The score records quiz and neuron challenge results.

## Art and font credits

The [MIT License](../../LICENSE) covers the original game code, tests, launchers, and web interface code. The Steins;Gate artwork follows its rights holders’ terms. The Spriters Resource archives the source images below.

- *Steins;Gate (Steam HD Edition)*, archived by Adrot. [Future Gadget Laboratory](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107557/), [Kurisu](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107532/), [Daru](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107534/), [Mayuri](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107547/), [phone](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107517/), and [divergence meter](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/asset/107527/).
- *Steins;Gate: Linear Bounded Phenogram*, archived by delta. [Okabe](https://www.spriters-resource.com/pc_computer/steinsgatelinearboundedphenogram/asset/153185/).
- The bundled fonts use the SIL Open Font License 1.1. [Instrument Serif](web/assets/instrument-serif-OFL.txt) · [Instrument Sans](web/assets/instrument-sans-OFL.txt) · [IBM Plex Mono](web/assets/ibm-plex-OFL.txt)

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
- Automated Chromium playthroughs covered the prologue, D-Mail phone, backlog, all four missions, scoring, reset, replay, and summary downloads at desktop and phone widths.

Before submission, play all four missions on your computer and ask another teammate to try the game. Record feedback and any corrections in the QA log. Downloaded summaries are not a substitute for an independent learner trial.

## Repository location

This game lives at `interactive-learning/python-game/` in the Aleksandria repository. It is an optional interactive supplement, not a replacement for the Study Guide or Test Bank.

## AI-use disclosure

The initial implementation and its tests were generated with AI assistance at the Quality Lead's request. The Operation World Line interface and mission framing also used AI assistance. Team review, adaptation, and the independent learner trial should be documented before submission.
