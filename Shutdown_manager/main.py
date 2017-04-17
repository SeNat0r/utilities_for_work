from manager import storage
import socket


# Создание соединения
class Socket(object):
    def __init__(self, port):
        self.port = port
        self.addres = None

    def connect(self):
        """Создание соединения"""
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', self.port))
        s.listen(2)
        conn, adr = s.accept()
        self.addres = adr[0]
        return conn

    def send(self, data, adr):
        """Отправка данных"""
        s = socket.socket()
        s.connect((adr, self.port))
        s.send(data.encode())


# Действия
class Manager(object):
    def __init__(self):
        self.manager_key = '666'


class Server(object):
    def __init__(self, s):
        self.sock = s

    def listen(self):
        while True:
            with self.sock.connect() as conn:
                d = conn.recv(1024).decode()
                if d == '111':
                    self.connect_check()

    def connect_check(self):
        self.sock.send('666', self.sock.addres)


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
b.listen()