import asyncio
import websockets
import json

# WebSocket client
async def send_messages():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Connected to WebSocket server at ws://localhost:8765")
        while True:
            # Get user input
            message = input("Enter a message (or 'exit' to quit): ")
            if message.lower() == "exit":
                break
            
            # Create a JSON object
            data = {
                "message": message,
                "timestamp": asyncio.get_event_loop().time()
            }
            
            # Send the JSON object to the server
            await websocket.send(json.dumps(data))
            
            # Receive the server's response
            response = await websocket.recv()
            print(f"Received: {response}")

# Run the client
print("Starting WebSocket client...")
asyncio.run(send_messages())