# Local Chat Service

Local Chat Service is a simple Python application for chatting within a local network. It facilitates message exchange between a server and clients, enabling two-way communication.

## Features

- Chat functionality within a local network
- Support for multiple clients (up to 5)
- Dummy data transmission from server to clients (using Faker)
- Parallel processing using threads
- Error handling and server shutdown process

## Requirements

- Python 3.x
- `socket` module
- `threading` module
- `faker` module (installation required: `pip install faker`)

## Usage

1. Start the server by running `server.py`:

```bash
python3 server.py
```

2. In a separate terminal window, run `client.py` to start a client:

```bash
python3 client.py
```

3. Enter messages on the client side and press Enter to send them to the server.
4. Response messages from the server will be displayed on the client side.
5. Enter `end` on the client side to terminate the connection with the server.
6. Press Ctrl+C on the server side to shut down the server.

## Code Explanation

### server.py
- `handle_client_connection` function: Handles connections with clients. Receives messages from clients and sends response messages (dummy data using Faker).
- `start_server` function: Starts the server and accepts new client connections. Creates a separate thread for each client connection and calls the `handle_client_connection` function.

### client.py
- The client connects to the server and sends input messages from the user to the server.
- It receives and displays response messages from the server.
- Entering `end` terminates the client's connection with the server.
