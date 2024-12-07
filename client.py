import socket

def start_client():
    try:
        # Step 1: Create a socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[INFO] Client socket created successfully.")

        # Step 2: Connect to the server
        host = '127.0.0.1'  # Server IP
        port = 65432  # Server port
        client_socket.connect((host, port))
        print(f"[INFO] Connected to server at {host}:{port}")

        # Step 3: Message exchange
        while True:
            # Input message to send to the server
            message = input("Enter message to send (type 'exit' to disconnect): ")
            if message.lower() == 'exit':
                print("[INFO] Disconnecting from server...")
                break

            # Send message to the server
            client_socket.send(message.encode('utf-8'))

            # Receive and print the server's response
            response = client_socket.recv(1024).decode('utf-8')
            print(f"[SERVER]: {response}")

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        # Step 4: Graceful shutdown
        client_socket.close()
        print("[INFO] Client socket closed.")

if __name__ == "__main__":
    start_client()
