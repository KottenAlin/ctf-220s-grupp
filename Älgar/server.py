# ================ Server Code (host.py) ================
import socket
import threading

# Server configuration
HOST = '0.0.0.0'  
PORT = 55555

# Store connected clients {user_id: socket}
clients = {}
lock = threading.Lock()

def handle_client(client_socket):
    try:
        # Get user ID
        user_id = client_socket.recv(1024).decode('utf-8')
        if not user_id:
            return
            print(f"New user {user_id} requesting connection")
        # Check if user ID is already connected
        with lock:
            if user_id in clients:
                client_socket.send("ERROR: ID already in use".encode('utf-8'))
                client_socket.close()
                return
            clients[user_id] = client_socket

        client_socket.send("SUCCESS: Connected to server".encode('utf-8'))

        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            # Parse message format: recipient_id:message
            if ':' not in data:
                continue
            recipient_id, message = data.split(':', 1)

            # Forward message to recipient
            with lock:
                recipient_socket = clients.get(recipient_id)
                if recipient_socket:
                    try:
                        recipient_socket.send(f"From {user_id}: {message}".encode('utf-8'))
                    except:
                        pass
                else:
                    client_socket.send(f"ERROR: User {recipient_id} not found".encode('utf-8'))

    except ConnectionResetError:
        pass
    finally:
        with lock:
            if user_id in clients:
                del clients[user_id]
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        user_id = client_socket.recv(1024).decode('utf-8')
        print(f"User {user_id} connected from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    print("Starting server...")
    start_server()
    print("Server stopped")