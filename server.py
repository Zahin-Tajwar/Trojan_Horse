import socket

HOST = '' #Enter ipv4 address 
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

server.listen()

client, address = server.accept()

while True:
    print(f"Connected to {address}")
    cmd = input("Enter a command:")
    client.send(cmd.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
