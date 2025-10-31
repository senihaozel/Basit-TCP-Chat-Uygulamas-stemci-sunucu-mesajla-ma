import socket

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    msg = input("Sen: ")
    client_socket.sendall(msg.encode())
    data = client_socket.recv(1024).decode()
    print("Sunucu:", data)

client_socket.close()
