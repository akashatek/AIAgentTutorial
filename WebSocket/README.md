# WebSocket

Reference:
 * [WebSocket](https://websockets.readthedocs.io/en/10.0/intro/index.html)

Launch you Server Layer (python) and your Presentation Layer (NodeJS) in 2 separate terminal.
Go to [http://127.0.01:8080/](http://127.0.0.1:8080/)

PS: you can also use Client Layer (python) to debug.

## Server Layer

Server.py
```
cd server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 server.py
```

## Client Layer

Client.py
```
cd client
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 client.py
```

## Presentation Layer

```
cd presentation
npm init -y
npm install --includeing-dev http-server
http-server -c-1 .
```