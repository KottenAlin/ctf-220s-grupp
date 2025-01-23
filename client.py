# ================ Client Code (client.py) ================
import socket
import threading

# Server configuration (change to your server's IP)
SERVER_HOST = '10.22.5.222'  # Replace with your server's local IP
SERVER_PORT = 55555

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"\n{data}\nYou: ", end='')
        except ConnectionResetError:
            break

def start_client():
    
    user_id = input("Enter your unique ID: ")
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a new socket
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        client_socket.send(user_id.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        if "ERROR" in response:
            print(response)
            return
    except Exception as e:
        print(f"Connection error: {e}")
        return
    
 

    print("Connected to server! Commands:")
    print("- To send message: <recipient_id>:<message>")
    print("- Type 'exit' to quit")

    # Start receive thread
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()

    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break
        
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            print("Connection lost")
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()