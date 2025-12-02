const chatWindow = document.getElementById('chat-window');
const input = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');
const orb = document.getElementById('orb');
const riskStatus = document.getElementById('status-risk');
const riskScoreStatus = document.getElementById('status-risk-score');
const coherenceStatus = document.getElementById('status-coherence');
const toneStatus = document.getElementById('status-tone');

function appendMessage(text, role) {
  const div = document.createElement('div');
  div.className = `message ${role}`;
  div.textContent = text;
  chatWindow.appendChild(div);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function updateStatus(data) {
  const riskLevel = data?.risk_level || 'N/A';
  const riskScoreValue =
    typeof data?.risk_score === 'number' ? data.risk_score.toFixed(2) : 'N/A';
  const coherenceValue =
    typeof data?.coherence === 'number' ? data.coherence.toFixed(2) : 'N/A';
  const toneValue = data?.tone || 'N/A';

  if (riskStatus) {
    riskStatus.textContent = `Risk: ${riskLevel}`;
  }

  if (riskScoreStatus) {
    riskScoreStatus.textContent = `Score: ${riskScoreValue}`;
  }

  if (coherenceStatus) {
    coherenceStatus.textContent = `Coherence: ${coherenceValue}`;
  }

  if (toneStatus) {
    toneStatus.textContent = `Tone: ${toneValue}`;
  }
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

    updateStatus(data);

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
