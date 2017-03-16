import configparser
import socket
from subprocess import call


def test():
    call('rundll32.exe user32.dll,LockWorkStation', shell=False)


def conn():
    sock = socket.socket()
    sock.bind(('', 9595))
    sock.listen(2)
    conn, addr = sock.accept()
    data = conn.recv(1024).decode()
    return data


def manager_edit(addr):
    config = configparser.RawConfigParser()
    config.read('default.ini')
    config.set('DEFAULT', 'manager', addr)
    with open('default.ini', 'w') as configfile:
        config.write(configfile)


def config_init():
    config = configparser.RawConfigParser()
    config.read('default.ini')
    manager = config.get('DEFAULT', 'manager')
    return manager

while True:
    a = conn()
    test()
