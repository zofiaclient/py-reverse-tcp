import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 12345

sock.bind((HOST, PORT))

sock.listen()

conn, addr = sock.accept()
print("Accepted incoming connection from address:", addr)

while True:
    command = input('Enter a command >> ')

    if command == 'exit':
        break

    # Make sure to encode the command!
    conn.send(command.encode())

    # Let's receive a bigger message this time.
    msg = conn.recv(8096).decode()
    print(msg)

conn.close()
print("Connection terminated!")
