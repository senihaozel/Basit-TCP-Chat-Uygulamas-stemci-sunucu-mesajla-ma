import socket

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Sunucu dinliyor...")

conn, addr = server_socket.accept()
print(f"{addr} bağlandı.")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("İstemci:", data)
    msg = input("Sen: ")
    conn.sendall(msg.encode())

conn.close()
server_socket.close()
