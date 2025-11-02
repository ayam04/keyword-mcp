# keyword-mcp

A small example showing a simple keyword search client/server written in Python.

## Overview

This repository contains a minimal client and server pair that demonstrate a keyword-search interaction. It's intended as a lightweight example project you can run locally to explore simple request/response behavior.

## Files

- `server.py` - Simple server that accepts requests and searches for a provided keyword (example implementation).
- `client.py` - Simple client that sends a keyword to the server and prints the response.
- `requirements.txt` - Python dependencies (if any).

## Requirements

- Python 3.9+
- Install dependencies:

```pwsh
python -m pip install -r requirements.txt
```

If `requirements.txt` is empty or not needed, the above command is safe to run and will do nothing.

## Usage

1. Start the server (run in one terminal):

```pwsh
python server.py
```

2. In another terminal, run the client and pass a keyword to search for (example):

```pwsh
python client.py "your-keyword"
```

Adjust the commands above if your environment uses a specific Python executable (for example, `python3`).
