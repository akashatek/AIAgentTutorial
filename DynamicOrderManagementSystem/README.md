# Dynamic Order Management System

Reference: [LangGraph AI agents : Building a Dynamic Order Management System : A Step-by-Step Tutorial](https://ai.gopubby.com/langgraph-building-a-dynamic-order-management-system-a-step-by-step-tutorial-0be56854fc91)

## Development environment

Install the environment
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy *.env-example* file into *.env* file.    
Update the GROQ_API_KEY="..." environment variable.

Run the local web server.
```
.venv/bin/uvicorn main:app --reload
```

Reach out to your web browser: [http://localhost:8000/](http://localhost:8000/)