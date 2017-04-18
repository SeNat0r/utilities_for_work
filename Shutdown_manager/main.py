from manager import storage
import socket
import pickle


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
        pi_data = pickle.dumps(data)
        s.send(pi_data)


# Действия
class Manager(object):
    def __init__(self):
        self.manager_key = '666'


class Server(object):
    def __init__(self, s, db):
        self.sock = s
        self.db = db

    def listen(self):
        while True:
            with self.sock.connect() as conn:
                d = conn.recv(1024)
                pi_data = pickle.loads(d)
                if pi_data[0] == 'server':
                    if pi_data[1] == 'check':
                        self.connect_check()
                    if pi_data[1] == 'info':
                        self.add_comm(pi_data)

    def connect_check(self):
        self.sock.send('666', self.sock.addres)

    def add_comm(self, d):
        print('Info!!')
        storage.add_communication(self.db, d[2], self.sock.addres, d[3])





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


conn = storage.connect('base.db')
storage.initialize(conn)

s = Socket(9696)
b = Server(s, conn)
b.listen()
