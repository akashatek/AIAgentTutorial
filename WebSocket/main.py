from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import asyncio

app = FastAPI()

# In a real chatbot, you'd likely integrate with an NLP model or a rule-based system here
async def process_message(message: str) -> str:
    """
    Simulates a chatbot's response.
    """
    message = message.lower()
    if "hello" in message or "hi" in message:
        return "Hello there! How can I help you today?"
    elif "how are you" in message:
        return "I'm a bot, so I don't have feelings, but I'm ready to assist!"
    elif "time" in message:
        import datetime
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a great day."
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"

@app.get("/")
async def get():
    # Serves the HTML client
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>WebSocket Chatbot</title>
        <style>
            body { font-family: sans-serif; max-width: 800px; margin: 20px auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px; }
            #messages { list-style: none; padding: 0; margin-bottom: 15px; max-height: 400px; overflow-y: auto; border: 1px solid #eee; padding: 10px; border-radius: 4px; }
            #messages li { background: #f9f9f9; padding: 8px; margin-bottom: 5px; border-radius: 4px; }
            #messages li.user-message { background: #e0f7fa; text-align: right; }
            #messages li.bot-message { background: #ffe0b2; text-align: left; }
            #chat-form { display: flex; }
            #messageText { flex-grow: 1; padding: 10px; border: 1px solid #ccc; border-radius: 4px 0 0 4px; }
            #sendButton { padding: 10px 15px; background-color: #007bff; color: white; border: none; border-radius: 0 4px 4px 0; cursor: pointer; }
            #sendButton:hover { background-color: #0056b3; }
        </style>
    </head>
    <body>
        <h1>Simple Chatbot</h1>
        <ul id='messages'></ul>
        <form id="chat-form" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off" placeholder="Type your message..."/>
            <button id="sendButton">Send</button>
        </form>

        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");

            ws.onopen = function(event) {
                console.log("WebSocket connection opened.");
                appendMessage("bot", "Hello! I'm your simple chatbot. Ask me anything!");
            };

            ws.onmessage = function(event) {
                appendMessage("bot", event.data);
            };

            ws.onclose = function(event) {
                console.log("WebSocket connection closed:", event);
                appendMessage("bot", "Chatbot connection closed. Please refresh the page to reconnect.");
            };

            ws.onerror = function(event) {
                console.error("WebSocket error:", event);
                appendMessage("bot", "An error occurred with the chatbot connection.");
            };

            function sendMessage(event) {
                var input = document.getElementById("messageText");
                var message = input.value.trim();
                if (message) {
                    appendMessage("user", message);
                    ws.send(message);
                    input.value = ''; // Clear input field
                }
                event.preventDefault(); // Prevent form submission
            }

            function appendMessage(sender, text) {
                var messages = document.getElementById('messages');
                var li = document.createElement('li');
                li.textContent = text;
                li.classList.add(sender + '-message');
                messages.appendChild(li);
                messages.scrollTop = messages.scrollHeight; // Scroll to the bottom
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received from client: {data}")
            
            # Process the message with your chatbot logic
            bot_response = await process_message(data)
            
            await websocket.send_text(bot_response)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"WebSocket error: {e}")