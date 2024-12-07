import socket
import threading

def handle_client(conn):
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if not message:
                print("[INFO] Client disconnected.")
                break
            print(f"[CLIENT]: {message}")
            response = f"Server received: {message}"
            conn.send(response.encode('utf-8'))
        except Exception as e:
            print(f"[ERROR] {e}")
            break
    conn.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432))
    server_socket.listen(5)
    print("[INFO] Server is listening...")

    def server_commands():
        while True:
            command = input()
            if command.lower() == 'stop':
                print("[INFO] Stopping the server...")
                server_socket.close()
                break

    threading.Thread(target=server_commands).start()

    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"[INFO] Connection established with {addr}")
            threading.Thread(target=handle_client, args=(conn,)).start()
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        print("[INFO] Server socket closed.")

if __name__ == "__main__":
    start_server()
