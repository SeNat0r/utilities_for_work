import configparser
import socket
from subprocess import call


# def test():
#     call('rundll32.exe user32.dll,LockWorkStation', shell=False)
#
#
# def conn():
#     sock = socket.socket()
#     sock.bind(('', 9595))
#     sock.listen(2)
#     conn, addr = sock.accept()
#     data = conn.recv(1024).decode()
#     return data
#
#
# def manager_edit(addr):
#     config = configparser.RawConfigParser()
#     config.read('default.ini')
#     config.set('DEFAULT', 'manager', addr)
#     with open('default.ini', 'w') as configfile:
#         config.write(configfile)
#
#
# def config_init():
#     config = configparser.RawConfigParser()
#     config.read('default.ini')
#     manager = config.get('DEFAULT', 'manager')
#     return manager
#
# while True:
#     a = conn()
#     test()

# Создание соединения
class Connection(object):
    def __init__(self, conn, data, port):
        self.conn = conn
        self.sock = socket.socket()
        self.data = data
        self.port = port

    # Слушаем сокет
    def listen(self):
        self.sock.bind(('', self.port))
        self.sock(2)
        conn, addr = self.sock.accept()
        data = conn.recv(1024).decode()
        return data

    # Отправка данных
    def send(self, addr, data):
        with self.sock.connect((addr, self.port)):
            self.sock.send(data.encode())


# Работа с конфигом
class Config(object):
    def __init__(self, addr):
        self.config = configparser.RawConfigParser()
        self.addr = addr

    def init_config(self):
        pass


# Действие на тонком клиенте
class Action(object):
    @staticmethod
    def test():
        call('rundll32.exe user32.dll,LockWorkStation', shell=False)
