import socket


def connect(addr):
    cmd = 'aaa'
    sock = socket.socket()
    sock.connect((addr, 9595))
    sock.send(cmd.encode())
    sock.close()


connect('127.0.0.1')