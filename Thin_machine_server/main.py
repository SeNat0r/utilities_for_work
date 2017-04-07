import configparser
import socket
from subprocess import call


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

# Создание соединения
class Socket(object):
    def __init__(self, port):
        self.__sock = socket.socket()
        self.port = port
        self.conn = '192.168.0.201'

    # Биндим интерфейс, порт
    # Слушаем макс 2 соединения
    # получаем и декодируем пакеты по 1024 байта
    def listen(self):
        """Прослушка сокета"""
        self.__sock.bind(('', self.port))
        self.__sock.listen(2)
        conn, addr = self.__sock.accept()
        data = conn.recv(1024).decode()
        return data

    def send(self, data):
        """Отправка данных"""
        self.__sock.connect((self.conn, self.port))
        self.__sock.send(data.encode())
        self.__sock.close()

    def check(self):
        s = socket.socket()
        try:
            s.connect((self.conn, self.port))
            return True
        except Exception as e:
            pass


class Manager(object):
    def __init__(self, s, key='666'):
        self.manager_key = key
        self.sock = s

    def connect_check(self):
        d = {'type': 'server', 'check': 1}
        self.sock.send(d)
        resp = self.sock.listen()
        if resp == self.manager_key:
            print('True')
            return True




# Работа с конфигом
# class Config(object):
#     def __init__(self, addr):
#         self.config = configparser.RawConfigParser()
#         self.addr = addr
#
#     def init_config(self):
#         pass


# Действие на тонком клиенте
class Server(object):
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port
        self.action_key = 123

    @staticmethod
    def action_block():
        """Закрытие соединения"""
        call('TASKKILL /IM "wfica32.exe"', shell=False)

    @staticmethod
    def action_off():
        """Закрытие соединения + гибернация тонкого клиента"""
        call('TASKKILL /IM "wfica32.exe"', shell=False)
        call('shutdown /h /f -t 5', shell=False)

    @classmethod
    def do(cls, data):
        """Разрешенные действия"""
        actions = {
            '1': cls.action_block,
            '2': cls.action_off,
            '3': cls.action_off
        }
        action = actions.get(data)
        if action:
            return action()

    def start(self):
        """Запуск сервера"""
        while True:
            conn = Socket(self.port)
            d = conn.listen()
            Server.do(d)

s = Socket(9595)
m = Manager(s)