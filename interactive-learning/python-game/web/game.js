'use strict';

const $ = (id) => document.getElementById(id);
const TRAINING_INDEX = 5;
const CHECK_COUNT = 8;
const LOSS_GOAL = 0.30;
const CHAPTERS = [
  { name: 'The duplicate', art: 'lab-evening', room: 'Akihabara', time: '18:52' },
  { name: 'The wrong digit', art: 'lab-night', room: 'Akihabara', time: '19:04' },
  { name: 'PhoneWave workbench', art: 'lab-workbench', room: 'Workbench', time: '19:17' },
  { name: 'One last check', art: 'lab-night', room: 'Akihabara', time: '19:36' },
];
const ACTORS = {
  okabe: 'Rintaro Okabe', 'okabe-phone': 'Rintaro Okabe',
  kurisu: 'Kurisu Makise', daru: 'Daru', mayuri: 'Mayuri Shiina',
};
const OPENING = [
  ['okabe-phone', 'My phone buzzed. The message was dated tomorrow.'],
  ['kurisu', 'Then check the files first. If the results are wrong, sending them back gives us the same mistake a day earlier.'],
  ['daru', 'I copied the handwriting samples off the IBN. One of these scans looks familiar.'],
];
// The reply order matches the answer indices in the Python question bank.
const QUESTION_SCENES = [
  { chapter: CHAPTERS[0], actor: 'daru',
    prompt: 'Same scan in the training folder and the test folder. What do you want me to do with it?',
    replies: ['Leave it in both folders.', 'Remove the duplicate from the test set.', 'Copy the whole training set over.'] },
  { chapter: CHAPTERS[0], actor: 'daru',
    prompt: 'This scan is a five. When I feed it into the model, what actually goes in?',
    replies: ['Send the answer, five.', 'Send the writer’s name.', 'Send the pixels. Keep five as the training target.'] },
  { chapter: CHAPTERS[0], actor: 'daru',
    prompt: 'This pixel is 128 out of 255. What do we get if we divide it by 255?',
    replies: ['About 0.502.', '128.0.', '255.0.'] },
  { chapter: CHAPTERS[1], actor: 'kurisu',
    prompt: 'The scan is a five. The model gave three a score of 0.60 and five 0.30. The other digits add up to 0.10. Which digit did the model pick?',
    replies: ['Five. That’s what the label says.', 'Three. It got the highest score.', 'It didn’t pick a digit.'] },
  { chapter: CHAPTERS[1], actor: 'kurisu',
    prompt: 'We’ve calculated the loss. What has to happen before the model can try again?',
    replies: ['Backpropagation finds the gradients. The optimizer updates the parameters.', 'Store the answer in every neuron.', 'Feed the test labels in as pixels.'] },
  { chapter: CHAPTERS[3], actor: 'mayuri',
    prompt: 'What if I write a number it hasn’t seen before? Does the lower training loss tell us how well it’ll read mine?',
    replies: ['Yes. Lower training loss proves it’ll read yours.', 'We need to try it on handwriting held back from training.', 'Yes. Let’s run the same training scans again.'] },
  { chapter: CHAPTERS[3], actor: 'kurisu',
    prompt: 'It keeps misreading some people’s handwriting. What would you put in the report?',
    replies: ['Leave those mistakes out.', 'Say it works equally well for everyone.', 'Check who’s represented, report the errors by group, and keep human review.'] },
];
const MAIL = [
  { from: 'From: Kurisu  /  29 Jul, 18:52', subject: 'Check the test folder',
    body: 'The IBN copies ended up in both folders. Check the handwriting model before we send its results back.\n\nStart with Daru’s scans.' },
  { from: 'From: Rintaro Okabe  /  28 Jul, 19:36', subject: 'Re: Check the test folder',
    body: 'The duplicate is out of the test folder. The neuron test is done. We’ll check the handwriting it hasn’t seen before we report accuracy.' },
];

let questions = [];
let index = 0;
let score = 0;
let steps = 0;
let neuronState;
let currentMail = MAIL[0];

async function api(path, data) {
  const options = data === undefined ? undefined : {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  };
  const response = await fetch(path, options).catch(() => null);
  if (!response || !response.ok) {
    throw new Error('Couldn’t reach the game. Keep the Python program running and try again.');
  }
  return response.json();
}

function updateProgress(completed) {
  $('check-count').textContent = `${completed} / ${CHECK_COUNT} checks`;
  $('score').textContent = `Score ${score} / 10`;

  // Divergence follows the story's progress. The score is tracked separately.
  const start = 0.571046;
  const end = 1.048596;
  const value = (start + (end - start) * completed / CHECK_COUNT).toFixed(6);
  const meter = $('divergence');
  meter.setAttribute('aria-label', value);
  meter.replaceChildren(...Array.from(value, (digit) => {
    const tube = document.createElement('span');
    tube.className = 'nixie-digit';
    tube.setAttribute('aria-hidden', 'true');
    tube.style.backgroundPositionX = `${digit === '.' ? 100 : Number(digit) * 10}%`;
    return tube;
  }));
  $('divergence-label').lastElementChild.textContent = completed === CHECK_COUNT ? 'SG' : 'α';
}

function setScene(view, chapter, actor) {
  $('game').dataset.view = view;
  $('error').textContent = '';
  $('scene-room').textContent = chapter.room;
  $('scene-date').textContent = chapter.date ?? '28 JUL 2010';
  $('scene-time').textContent = chapter.time;
  $('backdrop').style.backgroundImage = `url("assets/${chapter.art}.webp")`;
  const portrait = $('portrait');
  if (portrait.dataset.actor !== actor) {
    portrait.src = `assets/${actor}.webp`;
    portrait.dataset.actor = actor;
  }
  $('footer-context').textContent = chapter.name;
}

function recordLine(speaker, text) {
  const line = document.createElement('li');
  const name = document.createElement('strong');
  name.textContent = speaker;
  line.append(name, document.createTextNode(`  ${text}`));
  $('log-list').appendChild(line);
}

function render(view, content) {
  const screen = $('screen');
  screen.className = `screen ${view}-screen`;
  screen.innerHTML = content;
  return $('screen-title');
}

function showDialogue(chapter, actor, text, buttonLabel, next) {
  setScene('dialogue', chapter, actor);
  const speaker = ACTORS[actor];
  render('dialogue', `
    <div class="dialogue-box">
      <div><h1 class="speaker" id="screen-title" tabindex="-1"></h1><p class="dialogue-line" id="dialogue-line"></p></div>
      <button class="scene-button dialogue-next" id="next" type="button"></button>
    </div>`).textContent = speaker;
  $('dialogue-line').textContent = text;
  recordLine(speaker, text);
  const button = $('next');
  button.append(document.createTextNode(`${buttonLabel} `), nextArrow());
  button.onclick = next;
  focusScene();
}

function focusScene() {
  $('screen-title').focus();
  $('scene-place').scrollIntoView({ block: 'start' });
}

function nextArrow() {
  const arrow = document.createElement('span');
  arrow.setAttribute('aria-hidden', 'true');
  arrow.textContent = '▸';
  return arrow;
}

function addContinue(container, label, action) {
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'scene-button';
  button.append(document.createTextNode(`${label} `), nextArrow());
  button.onclick = action;
  $(container).appendChild(button);
  button.focus();
}

function showMail() {
  $('mail-title').textContent = currentMail === MAIL[0] ? 'Received mail' : 'Sent mail';
  $('mail-from').textContent = currentMail.from;
  $('mail-subject').textContent = currentMail.subject;
  $('mail-body').textContent = currentMail.body;
  $('mail').showModal();
  $('mail-body').parentElement.scrollTop = 0;
}

function showOpening(line = 0) {
  const [actor, text] = OPENING[line];
  if (line === 0) {
    showDialogue({ ...CHAPTERS[0], name: 'Tomorrow’s mail' }, actor, text, 'Read the D-Mail', () => {
      $('open-mail').hidden = false;
      recordLine('D-Mail', `${currentMail.subject}. ${currentMail.body.replace(/\n+/g, ' ')}`);
      $('mail').addEventListener('close', () => showOpening(1), { once: true });
      showMail();
    });
    return;
  }
  const next = line === OPENING.length - 1 ? showQuestion : () => showOpening(line + 1);
  showDialogue(line === 1 ? { ...CHAPTERS[0], name: 'Tomorrow’s mail' } : CHAPTERS[0], actor, text, 'Continue', next);
}

async function start() {
  const button = $('start');
  button.disabled = true;
  $('error').textContent = '';
  try {
    questions = await api('questions');
    $('footer-controls').hidden = false;
    $('footer-status').hidden = false;
    showOpening();
  } catch (error) {
    $('error').textContent = error.message;
    button.disabled = false;
  }
}

function showQuestion() {
  const { chapter, actor, prompt, replies } = QUESTION_SCENES[index];
  const question = questions[index];
  const completed = index < TRAINING_INDEX ? index : index + 1;
  let attempts = 0;

  setScene('question', chapter, actor);
  updateProgress(completed);
  render('question', `
    <div class="dialogue-box">
      <div>
        <h1 class="speaker" id="screen-title" tabindex="-1"></h1>
        <p class="dialogue-line" id="dialogue-line"></p>
        <div class="feedback" id="feedback" aria-live="polite" aria-atomic="true"></div>
      </div>
      <div class="actions dialogue-next" id="question-actions"></div>
    </div>
    <div class="choices" id="choices" role="group" aria-labelledby="dialogue-line">
      <p class="caption choice-label">Your reply</p>
    </div>`).textContent = ACTORS[actor];
  $('dialogue-line').textContent = prompt;
  recordLine(ACTORS[actor], prompt);

  const buttons = question.options.map((original, number) => {
    const option = replies[number] ?? original;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'choice';
    const letter = document.createElement('span');
    letter.className = 'choice-letter';
    letter.textContent = String.fromCharCode(65 + number);
    letter.setAttribute('aria-hidden', 'true');
    const label = document.createElement('span');
    label.textContent = option;
    button.append(letter, label);
    button.onclick = async () => {
      $('error').textContent = '';
      buttons.forEach((choice) => { choice.disabled = true; });
      try {
        const result = await api('answer', { question: index, option: number });
        attempts++;
        button.classList.add(result.correct ? 'correct' : 'wrong');
        const status = document.createElement('span');
        status.className = 'reply-status';
        status.textContent = result.correct ? 'Accepted' : 'Try again';
        label.append(status);
        const feedback = result.correct ? 'Correct.' : 'Try again.';
        showFeedback('feedback', feedback, result.explanation);
        recordLine('You', option);
        recordLine(ACTORS[actor], result.explanation);
        if (result.correct) {
          if (attempts === 1) score++;
          updateProgress(completed + 1);
          const label = index === questions.length - 1 ? 'Send the D-Mail' : 'Continue';
          addContinue('question-actions', label, () => {
            index++;
            if (index === TRAINING_INDEX) showTraining();
            else if (index === questions.length) showResults();
            else showQuestion();
          });
          return;
        }
      } catch (error) {
        $('error').textContent = error.message;
      }
      const available = buttons.filter((choice) => !choice.classList.contains('wrong'));
      available.forEach((choice) => { choice.disabled = false; });
      (button.disabled ? available[0] : button).focus();
    };
    $('choices').appendChild(button);
    return button;
  });
  focusScene();
}

function showFeedback(id, title, message) {
  const heading = document.createElement('strong');
  heading.textContent = title;
  $(id).replaceChildren(heading, document.createTextNode(` ${message}`));
}

function showTraining() {
  const prompt = 'Let’s start with one neuron. Set the learning rate, take a step, and get the loss below 0.30.';
  setScene('training', CHAPTERS[2], 'kurisu');
  render('training', `
    <section class="workbench" aria-labelledby="screen-title">
      <p class="caption">PhoneWave workbench</p>
      <h1 id="screen-title" tabindex="-1">Train a neuron</h1>
      <p class="workbench-guide"><strong>Kurisu</strong> · ${prompt}</p>
      <dl class="metrics">
        <div><dt>Loss</dt><dd id="loss">—</dd></div>
        <div><dt>Prediction</dt><dd id="output">—</dd></div>
        <div><dt>Weight</dt><dd id="weight">—</dd></div>
        <div><dt>Bias</dt><dd id="bias">—</dd></div>
      </dl>
      <div class="training-controls">
        <label for="rate">Learning rate <output id="rate-label" for="rate">0.50</output></label>
        <input id="rate" type="range" min="0.1" max="1" step="0.1" value="0.5">
      </div>
      <details class="math-details">
        <summary>Experiment notes</summary>
        <p>The input and target are both 1. The prediction is p = sigmoid(w × x + b) and the binary cross-entropy loss is −log(p). The gradients are dL/dw = (p − y) × x and dL/db = p − y. Subtract the learning rate times each gradient to update its parameter.</p>
      </details>
      <div class="actions">
        <button class="scene-button" id="train" type="button">Run one training step</button>
        <button class="scene-button secondary" id="reset" type="button">Reset neuron</button>
      </div>
      <div class="feedback" id="train-feedback" aria-live="polite" aria-atomic="true"></div>
      <div class="actions" id="train-actions"></div>
    </section>`);
  recordLine(ACTORS.kurisu, prompt);
  $('rate').oninput = () => { $('rate-label').value = Number($('rate').value).toFixed(2); };
  $('train').onclick = train;
  $('reset').onclick = async () => {
    await resetNeuron();
    $('reset').focus();
  };
  focusScene();
  resetNeuron();
}

function lockTraining(locked) {
  for (const id of ['rate', 'train', 'reset']) $(id).disabled = locked;
}

async function resetNeuron() {
  lockTraining(true);
  $('error').textContent = '';
  try {
    neuronState = await api('neuron', { weight: -1, bias: 0 });
    steps = 0;
    $('rate').value = '0.5';
    $('rate-label').value = '0.50';
    $('train-feedback').replaceChildren();
    paintNeuron(neuronState);
  } catch (error) {
    $('error').textContent = error.message;
  }
  lockTraining(false);
  $('train').disabled = !neuronState;
}

function paintNeuron(state) {
  $('output').textContent = state.prediction.toFixed(3);
  $('loss').textContent = state.loss.toFixed(4);
  $('weight').textContent = state.weight.toFixed(3);
  $('bias').textContent = state.bias.toFixed(3);
}

async function train() {
  lockTraining(true);
  $('error').textContent = '';
  try {
    neuronState = await api('step', {
      weight: neuronState.weight,
      bias: neuronState.bias,
      rate: Number($('rate').value),
    });
    steps++;
    paintNeuron(neuronState);
    const { loss, previous_loss: previousLoss } = neuronState;
    const message = `Loss ${previousLoss.toFixed(4)} → ${loss.toFixed(4)}. Weight and bias updated.`;
    if (loss < LOSS_GOAL) {
      showFeedback('train-feedback', `Step ${steps}.`, `${message} Goal reached.`);
      addContinue('train-actions', 'Collect 3 points and continue', () => {
        score += 3;
        showQuestion();
      });
      return;
    }
    showFeedback('train-feedback', `Step ${steps}.`, message);
  } catch (error) {
    $('error').textContent = error.message;
  }
  lockTraining(false);
  $('train').focus();
}

function showResults() {
  const closing = 'The D-Mail went through. Next time they open the test folder, they’ll know what to check.';
  currentMail = MAIL[1];
  updateProgress(CHECK_COUNT);
  setScene('results', { name: 'After the jump', art: 'lab-morning', room: 'Akihabara', date: '29 JUL 2010', time: '08:03' }, 'okabe');
  render('results', `
    <section class="workbench" aria-labelledby="screen-title">
      <p class="caption">D-Mail sent</p>
      <h1 id="screen-title" tabindex="-1">Your score is ${score} / 10</h1>
      <p class="workbench-guide"><strong>Okabe</strong> · ${closing}</p>
      <ul>
        <li>Keep training and test examples separate.</li>
        <li>Backpropagation computes gradients. The optimizer uses them to update parameters.</li>
        <li>Evaluate on held-out data to measure generalization.</li>
      </ul>
      <p class="math-details">The score reflects your answers and the neuron challenge. Model accuracy requires testing on unseen examples.</p>
      <div class="actions">
        <button class="scene-button" id="replay" type="button">Play again</button>
        <button class="scene-button secondary" id="save" type="button">Save learning summary</button>
      </div>
    </section>`);
  recordLine(ACTORS.okabe, closing);
  $('replay').onclick = () => location.reload();
  $('save').onclick = saveSummary;
  focusScene();
}

function saveSummary() {
  const text = `Aleksandria Learning Lab
Operation World Line
Completed: ${new Date().toLocaleString()}
Quiz first-try score: ${score - 3}/7
Neuron challenge: 3/3
Training steps: ${steps}
Total: ${score}/10
This is a local game summary, not evidence of independent teammate review.
`;
  const download = document.createElement('a');
  download.href = URL.createObjectURL(new Blob([text], { type: 'text/plain' }));
  download.download = 'aleksandria-learning-summary.txt';
  download.click();
  setTimeout(() => URL.revokeObjectURL(download.href), 1000);
}

updateProgress(0);
$('start').onclick = start;
$('title-credits').onclick = () => $('credits').showModal();
$('open-log').onclick = () => $('log').showModal();
$('open-mail').onclick = showMail;
