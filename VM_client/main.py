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

    def manager_check(self):
        d = ['client', 'check']
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
#     # def __init__(self, addr):
#     #     self.addr = addr
#
#     @staticmethod
#     def get_config():
#         """Получение значений конфигураций из ini файла"""
#         config = configparser.RawConfigParser()
#         config.read('default.ini')
#         manager = config.get('DEFAULT', 'manager')
#         tc = config.get('DEFAULT', 'thin_client')
#         # return manager, tc
#         return tc
#
#         # def edit_config_tc(self):
#         #     config = configparser.RawConfigParser()
#         #     config.read('default.ini')
#         #     config.set('DEFAULT', 'thin_client', self.addr)
#         #     with open('default.ini', 'w') as configfile:
#         #         config.write(configfile)


class Action(object):
    pass


