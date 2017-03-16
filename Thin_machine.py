import socket
from subprocess import call


def test():
    call('rundll32.exe user32.dll,LockWorkStation', shell=False)


def conn(client):
    sock = socket.socket()
    sock.bind((client, 9595))
    sock.listen(2)
    conn, addr = sock.accept()
    data = conn.recv(1024).decode()
    return data


while True:
    a = conn('')
    test()