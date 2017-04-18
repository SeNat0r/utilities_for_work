import configparser
import socket
from subprocess import call
import pickle
from time import sleep


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


class Server(object):
    def __init__(self, port):
        self.port = port
        self.sock = Socket(self.port)
        self.mngr = Manager(self.sock)
        self.action_key = 123

    # def send_info(self):
    #     info = ['server', 'info', socket.gethostname(), self.action_key]
    #     self.sock.send(info, self.mngr.manager_adr)
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


class Client(object):
    def __init__(self, sock, mngr, srvr):
        self.sock = sock
        self.manager = mngr
        self.server = srvr

    def listen(self):
        while True:
            with self.sock.connect() as conn:
                d = conn.recv(1024)
                pi_data = pickle.loads(d)
                if pi_data[0] == 'manager':
                    if pi_data[1] == 'a_key':
                        pass
                    elif pi_data[1] == 'server':
                        pass
            sleep(1)


s = Socket(9696)
m = Manager(s)
print(m.manager_check())


