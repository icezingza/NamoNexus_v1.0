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
      appendMessage(`Blocked: ${JSON.stringify(data.detail || data)}`, 'namo');
    } else {
      const reflection = data.result?.reflection?.reflection || '...';
      const tone = data.result?.reflection?.tone || 'neutral';
      appendMessage(`${tone.toUpperCase()}: ${reflection}`, 'namo');
    }
  } catch (err) {
    appendMessage('Error contacting NaMo Nexus.', 'namo');
  } finally {
    orb.classList.remove('recalibrating');
  }
}

sendBtn.addEventListener('click', sendMessage);
input.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') sendMessage();
});
