// This file manages the backend communication with the server (Flask or similar)

function sendToBackend(message) {
    // Here you can implement logic to communicate with your backend
    // For example, a fetch request to a Flask server running locally
    fetch('http://localhost:5000/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response from server:', data);
        // Handle server response here
    })
    .catch(err => console.log('Error:', err));
}