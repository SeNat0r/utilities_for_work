from manager import storage
import socket


# Создание соединения
class Socket(object):
    def __init__(self, port):
        self.destination = ('127.0.0.1', port)

    def connect(self):
        """Создание соединения"""
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(self.destination)
        s.listen(2)
        conn, adr = s.accept()
        return conn

    def send(self, data):
        """Отправка данных"""
        s = socket.socket()
        s.connect(self.destination)
        s.send(data.encode())


# Действия
class Manager(object):
    def __init__(self):
        self.manager_key = '666'


class Server(object):
    def __init__(self, s):
        self.sock = s

    def connect_check(self):
        while 1:
            with self.sock.connect() as conn:
                abv = conn.recv(1024).decode()
                if abv == '111':
                    self.sock.send('666')


                # @staticmethod
                # def get_tc(conn):
                #     for idx in storage.all_idx(conn):
                #         Socket.destination.append(idx)
                #         # Connection.send(idx['TC_ip'])
                #
                # # Отправка значений конфига виртуальной машине
                # @staticmethod
                # def send_tc_ip(comm):
                #     for i in Socket.destination:
                #         Socket.send(comm, i['TC_ip'], i['VM_ip'])

#
# conn = storage.connect('base.db')
# storage.initialize(conn)

s = Socket(9696)
b = Server(s)
b.connect_check()