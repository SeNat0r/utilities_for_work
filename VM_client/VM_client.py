import socket
import configparser


def connect(addr):
    cmd = 'aaa'
    sock = socket.socket()
    sock.connect((addr, 9595))
    sock.send(cmd.encode())
    sock.close()


def manager_edit(addr):
    config = configparser.RawConfigParser()
    config.read('default.ini')
    config.set('DEFAULT', 'manager', addr)
    with open('default.ini', 'w') as configfile:
        config.write(configfile)


def tm_edit(addr):
    config = configparser.RawConfigParser()
    config.read('default.ini')
    config.set('DEFAULT', 'thin_client', addr)
    with open('default.ini', 'w') as configfile:
        config.write(configfile)


def config_init():
    config = configparser.RawConfigParser()
    config.read('default.ini')
    manager = config.get('DEFAULT', 'manager')
    tm = config.get('DEFAULT', 'thin_client')
    return manager, tm


manager, vm = config_init()

connect('127.0.0.1')
