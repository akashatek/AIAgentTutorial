// --- WebSocket Setup ---
            // IMPORTANT: Ensure this URL matches your Python server's WebSocket address and port
            const websocketUrl = "ws://localhost:8765";
            let ws; // Declare ws variable globally to manage connection

            const messagesContainer = document.getElementById('messages');
            const messageInput = document.getElementById('messageInput');
            const chatForm = document.getElementById('chatForm');

            function connectWebSocket() {
                // Close existing connection if any before creating a new one
                if (ws && (ws.readyState === WebSocket.OPEN || ws.readyState === WebSocket.CONNECTING)) {
                    ws.close();
                }

                ws = new WebSocket(websocketUrl);

                ws.onopen = (event) => {
                    console.log("WebSocket connected:", event);
                    // The bot sends its initial greeting from the server side, so no need for client-side here
                };

                ws.onmessage = (event) => {
                    console.log("Message from server:", event.data);
                    // Determine if it's a bot message (starts with "Bot: ") or a generic server message
                    if (event.data.startsWith("Bot: ")) {
                        appendMessage("bot", event.data.substring(5)); // Remove "Bot: " prefix for display
                    } else {
                        appendMessage("bot", event.data); // Fallback for other server messages
                    }
                };

                ws.onclose = (event) => {
                    console.warn("WebSocket disconnected:", event);
                    if (event.wasClean) {
                        appendMessage("bot", "Chatbot disconnected gracefully. Code: " + event.code);
                    } else {
                        appendMessage("bot", "Chatbot disconnected unexpectedly. Trying to reconnect in 3 seconds...");
                        // Attempt to reconnect after a short delay for unexpected closures
                        setTimeout(connectWebSocket, 3000);
                    }
                };

                ws.onerror = (error) => {
                    console.error("WebSocket error:", error);
                    appendMessage("bot", "An error occurred with the connection. Check server status.");
                    // Error usually precedes onclose, so onclose will handle reconnection
                };
            }

            // --- Chat Interface Logic ---

            // Function to add messages to the chat display
            function appendMessage(sender, message) {
                const li = document.createElement('li');
                li.textContent = message;
                li.classList.add(sender + '-message'); // Add class for styling (user-message or bot-message)
                messagesContainer.appendChild(li);
                // Scroll to the latest message
                messagesContainer.scrollTop = messagesContainer.scrollHeight;
            }

            // Handle sending messages when the form is submitted
            chatForm.addEventListener('submit', (event) => {
                event.preventDefault(); // Prevent page reload

                const message = messageInput.value.trim();
                if (message === '') {
                    return; // Don't send empty messages
                }

                if (ws && ws.readyState === WebSocket.OPEN) {
                    appendMessage("user", message); // Display user's message immediately
                    ws.send(message); // Send message to the server
                    messageInput.value = ''; // Clear input field
                } else {
                    appendMessage("bot", "Not connected to the chatbot. Please wait for connection or check server.");
                    console.warn("WebSocket not open. ReadyState:", ws ? ws.readyState : "Not initialized.");
                    // Optionally try to reconnect if not open when user tries to send
                    if (!ws || ws.readyState === WebSocket.CLOSED) {
                        connectWebSocket();
                    }
                }
            });

            // Initial connection attempt when the page loads
            document.addEventListener('DOMContentLoaded', connectWebSocket);