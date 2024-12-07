import socket
import sys

def port_scanner():
    try:
        # Step 1: Take user input for target host
        target = input("Enter the target host (localhost or scanme.nmap.org): ").strip()
        if target not in ['127.0.0.1', 'localhost', 'scanme.nmap.org']:
            raise ValueError("Unauthorized host. You can only scan localhost or scanme.nmap.org.")

        # Step 2: Take user input for port range
        start_port = int(input("Enter the starting port (1-65535): "))
        end_port = int(input("Enter the ending port (1-65535): "))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError("Invalid port range. Please enter valid port numbers (1-65535).")

        print(f"\n[INFO] Scanning host: {target} on ports {start_port}-{end_port}...\n")

        # Step 3: Loop through the port range and check each port
        open_ports = []
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set timeout for each connection
            result = sock.connect_ex((target, port))  # 0 = success, non-zero = failure

            if result == 0:
                print(f"[OPEN] Port {port} is open.")  # Open port found
                open_ports.append(port)
            else:
                print(f"[CLOSED] Port {port} is closed.")  # Closed port

            sock.close()  # Always close the socket after use

        # Step 4: Display the summary of open ports
        print("\n[SUMMARY] Open Ports:")
        if open_ports:
            print(", ".join(map(str, open_ports)))
        else:
            print("No open ports found.")  # If no open ports

    except ValueError as ve:
        print(f"[ERROR] {ve}")
    except socket.error as se:
        print(f"[ERROR] Socket error: {se}")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
    finally:
        print("[INFO] Port scanning completed.")

if __name__ == "__main__":
    port_scanner()
