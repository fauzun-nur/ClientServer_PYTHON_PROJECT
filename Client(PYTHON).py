import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Bind the server to the address and port
server_socket.bind(server_address)

# Listen for incoming connections (maximum 5 clients in the queue)
server_socket.listen(5)
print("Server is listening for connections...")

while True:
    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()
    
    print(f"Connection from {client_address}")
    
    # Receive data from the client
    data = client_socket.recv(1024)
    
    if not data:
        break
    
    # Send the received data back to the client
    client_socket.send(data)
    
    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()
