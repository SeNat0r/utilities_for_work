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
class Connection(object):
    def __init__(self, port):
        self.__sock = socket.socket()
        self.port = port

    # Биндим интерфейс, порт
    # Слушаем макс 2 соединения
    # получаем и декодируем пакеты по 1024 байта
    def do_listen(self):
        """Прослушка сокета"""
        self.__sock.bind(('', self.port))
        self.__sock.listen(2)
        conn, addr = self.__sock.accept()
        data = conn.recv(1024).decode()
        return data


# Работа с конфигом
# class Config(object):
#     def __init__(self, addr):
#         self.config = configparser.RawConfigParser()
#         self.addr = addr
#
#     def init_config(self):
#         pass


# Действие на тонком клиенте
class Action(object):
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

    @staticmethod
    def start(port):
        """Запуск сервера"""
        while True:
            conn = Connection(port)
            d = conn.do_listen()
            Action.do(d)

Action.start(9596)

