import configparser
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


def client_edit(addr):
    config = configparser.ConfigParser()
    config.set('DEFAULT', 'address', addr)
    with open('default.ini', 'w') as configfile:
        config.write(configfile)


def manager_edit(addr):
    config = configparser.RawConfigParser()
    config.read('default.ini')
    config.set('DEFAULT', 'manager', addr)
    with open('default.ini', 'w') as configfile:
        config.write(configfile)


manager_edit('444444')
while True:
    a = conn('')
    test()