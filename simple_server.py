import asyncio
import websockets
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# WebSocket server handler
async def handle_connection(websocket):
    print("Client connected")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            # Echo the message back to the client
            await websocket.send(f"Echo: {message}")
    except websockets.ConnectionClosed:
        print("Client disconnected")

# Start the WebSocket server
async def start_websocket_server():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("WebSocket server started at ws://localhost:8765")
        await asyncio.Future()  # Run forever

# Start the HTTP server
def start_http_server():
    handler = SimpleHTTPRequestHandler
    httpd = TCPServer(("localhost", 8000), handler)
    print("HTTP server started at http://localhost:8000")
    httpd.serve_forever()

# Run both servers
async def main():
    # Start the HTTP server in a separate thread
    import threading
    threading.Thread(target=start_http_server, daemon=True).start()

    # Start the WebSocket server
    await start_websocket_server()

# Run the program
asyncio.run(main())