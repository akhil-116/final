import socket

# Define the server's IP address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send data to the server
client_socket.sendall(b'Hello, VPN Server!')

# Receive data from the server
data = client_socket.recv(4096)
print(f"Received data from server: {data.decode()}")

# Close the connection
client_socket.close()
