import configparser
import socket
from subprocess import call
import pickle


# Создание соединения
class Socket(object):
    def __init__(self, port):
        self.port = port

    def connect(self):
        """Создание соединения"""
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', self.port))
        s.listen(2)
        conn, adr = s.accept()
        # print('адрес:', adr)
        return conn

    def send(self, data, adr):
        """Отправка данных"""
        s = socket.socket()
        s.connect((adr, self.port))
        pi_data = pickle.dumps(data)
        s.send(pi_data)

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
        self.manager_adr = '192.168.0.201'

    def connect_check(self):
        d = ['server', 'check']
        self.sock.send(d, self.manager_adr)

        while True:
            with self.sock.connect() as conn:
                resp = conn.recv(1024)
                pi_resp = pickle.loads(resp)
                if pi_resp == self.manager_key:
                    return True
                return False


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

#
s = Socket(9696)
m = Manager(s)
print(m.connect_check())
