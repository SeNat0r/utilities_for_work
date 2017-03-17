from manager import storage
import socket


# Создание соединения
class Connection(object):
    def __init__(self, data, port, destination):
        self.sock = socket.socket()
        self.data = data
        self.port = port
        self.destination = destination

    # Слушаем сокет
    def listen(self):
        self.sock.bind(('', self.port))
        self.sock(2)
        conn, addr = self.sock.accept()
        data = conn.recv(1024).decode()
        return data

    # Отправка данных
    def send(self, data):
        with self.sock.connect((self.destination, self.port)):
            self.sock.send(data.encode())


# Действия
class Action(object):
    def __init__(self, conn):
        self.conn = conn

    # Отправка значений конфига виртуальной машине
    def send_tc_ip(self):
        for idx in storage.all_idx(self.conn):
            Connection.destination = idx['VM_ip']
            Connection.send(idx['TC_ip'])


conn = storage.connect('base.db')
storage.initialize(conn)
Connection.port = 9595
Action.conn = conn
Action.send_tc_ip()

