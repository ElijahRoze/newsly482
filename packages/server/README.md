# Server

## Installation

Run this command to install python dependencies

```bash
cd packages/server
pip3 install -r requirements.txt
```

NOTE: You may need to setup a [virutal python environment](https://docs.python.org/3/library/venv.html).

## Running the server

First, you must run the database

```bash
cd packages/database
docker compose up
```

Then, to run the server, execute this command:

```bash
cd packages/server
fastapi dev main.py
```
