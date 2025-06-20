# ChatBot

Reference: [Deploying LangGraph with FastAPI: A Step-by-Step Tutorial](https://medium.com/@sajith_k/deploying-langgraph-with-fastapi-a-step-by-step-tutorial-b5b7cdc91385)

Components:
 * source code for HTML / Chatbot (python, langchain / langgraph)
 * Docker file to build / run docker   




![Graph PNG](./graph.png)

## Get source code
```
git clone https://github.com/akashatek/AIAgentTutorial.git
cd AIAgentTutorial/ChatBot
```

## Docker container environment

Build your docker image.
```
docker build -t akashatek/chatbot:1.04 .
docker push akashatek/chatbot:1.04
```

Update your environement variable *export GOOGLE_API_KEY="..."*

Run your docker container.
```
docker run -d -e GOOGLE_API_KEY --name chatbot -p 8000:8000 akashatek/chatbot:1.04
```
Reach out to your web browser: [http://localhost:8000/](http://localhost:8000/)

## Local environment

Install the environment
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Update your environement variable *export GOOGLE_API_KEY="..."*

Run the local web server.
```
.venv/bin/uvicorn main:app --reload
```

Reach out to your web browser: [http://localhost:8000/](http://localhost:8000/)