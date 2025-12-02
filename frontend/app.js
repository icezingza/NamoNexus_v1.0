const chatWindow = document.getElementById('chat-window');
const input = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');
const orb = document.getElementById('orb');

function appendMessage(text, role) {
  const div = document.createElement('div');
  div.className = `message ${role}`;
  div.textContent = text;
  chatWindow.appendChild(div);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  appendMessage(text, 'user');
  input.value = '';
  orb.classList.add('recalibrating');

  try {
    const res = await fetch('/reflect', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });

    const data = await res.json();

    if (!res.ok) {
      console.error('NaMo response error', data);
      appendMessage('NaMo could not process that request safely.', 'namo');
      return;
    }

    const reflectionText = data.reflection_text || data.message || 'NaMo is reflecting...';
    const tone = data.tone || 'neutral';
    const moralValue = typeof data.moral_index === 'number' ? data.moral_index.toFixed(2) : 'N/A';
    const namoReply = `${reflectionText}\nTone: ${tone} | Moral index: ${moralValue}`;

    appendMessage(namoReply, 'namo');
  } catch (err) {
    console.error('Network or parsing error', err);
    appendMessage('NaMo is temporarily unavailable. Please try again soon.', 'namo');
  } finally {
    orb.classList.remove('recalibrating');
  }
}

sendBtn.addEventListener('click', sendMessage);
input.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') sendMessage();
});
