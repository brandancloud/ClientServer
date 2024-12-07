### Client-Server Communication

- **Objective**: Establishes communication between a server and client using Python's `socket` library.
- **Server**:
  - Binds to a host and port.
  - Listens for incoming connections.
  - Handles client messages and sends responses.
- **Client**:
  - Connects to the server on a specific host and port.
  - Sends a message to the server.
  - Receives and processes the server's response.
- **Key Features**:
  - Proper socket initialization and connection handling.
  - Error handling for common connection issues.
  - Graceful shutdown and disconnection process.

---

### Port Scanner

- **Objective**: Scans a range of ports on a target host to check their status (open or closed).
- **Key Features**:
  - **Input Validation**: Ensures valid host and port range input.
  - **Port Status Check**: Attempts to connect to each port in the specified range.
  - **Result Reporting**: Displays open ports or informs if no open ports were found.
- **Functionality**:
  - Uses the `socket` library to check each port.
  - Provides a summary of open ports at the end of the scan.
  - Includes error handling for invalid inputs and unreachable hosts.
- **Ethical Scanning**: Scans only localhost and `scanme.nmap.org` to avoid legal issues.
