import socket
import configparser


# def connect(addr):
#     cmd = 'aaa'
#     sock = socket.socket()
#     sock.connect((addr, 9595))
#     sock.send(cmd.encode())
#     sock.close()
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
# def tm_edit(addr):
#     config = configparser.RawConfigParser()
#     config.read('default.ini')
#     config.set('DEFAULT', 'thin_client', addr)
#     with open('default.ini', 'w') as configfile:
#         config.write(configfile)
#
#
# def config_init():
#     config = configparser.RawConfigParser()
#     config.read('default.ini')
#     manager = config.get('DEFAULT', 'manager')
#     tm = config.get('DEFAULT', 'thin_client')
#     return manager, tm
#
#
# manager, thin = config_init()
#
# connect(thin)

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