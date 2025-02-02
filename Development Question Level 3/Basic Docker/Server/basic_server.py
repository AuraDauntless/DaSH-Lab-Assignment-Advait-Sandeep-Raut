import socket
server_socket=socket.socket()
print("Socket Created Successfully")

server_socket.bind(('localhost',9999))
server_socket.listen()
print("Waiting for connections")
while True:
    client_socket,addr=server_socket.accept()
    name=client_socket.recv(102444).decode()
    print("Connected with", addr," , ",name)
    client_socket.send(bytes("Welcome to DaSH Lab",'utf-8'))
    client_socket.close()
