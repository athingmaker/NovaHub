const chatBox = document.getElementById("chat-box");
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");

function displayMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

sendButton.addEventListener("click", () => {
    const message = messageInput.value.trim();
    if (message) {
        displayMessage(message, 'user');
        messageInput.value = ''; // Clear input field
        // Call backend to get a response
        getBotResponse(message);
    }
});

// Function to fetch bot response
function getBotResponse(userMessage) {
    fetch('http://localhost:5000/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data.response, 'bot');  // Display bot's response
    })
    .catch(error => {
        console.error('Error:', error);
        displayMessage('Sorry, something went wrong.', 'bot');
    });
}