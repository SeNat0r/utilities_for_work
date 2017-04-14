import configparser
import socket
from subprocess import call


# Создание соединения
class Socket(object):
    def __init__(self, port):
        self.destination = ('', port)

    # Биндим интерфейс, порт
    # Слушаем макс 2 соединения
    # получаем и декодируем пакеты по 1024 байта
    def listen(self):
        """Прослушка сокета"""
        with socket.socket() as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(self.destination)
            s.listen(2)

            # while True:
            #     conn, adr = s.accept()
            #
            #     with conn:
            #         data = conn.recv(1024).decode()
            #         if data:
            #             print(data)
            #             return data

    def send(self, data):
        """Отправка данных"""
        with socket.socket():
            s.connect(self.destination)
            s.send(data.encode())

            # def check(self):
            #     s = socket.socket()
            #     try:
            #         s.connect((self.conn, self.port))
            #         return True
            #     except Exception as e:
            #         pass


class Manager(object):
    def __init__(self, s, key='666'):
        self.manager_key = key
        self.sock = s

    def connect_check(self):
        # d = {'type': 'server', 'check': '1'}
        d = '111'
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
            d = conn.get_data()
            Server.do(d)


s = Socket(9696)
m = Manager(s)

