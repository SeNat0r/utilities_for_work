from manager import storage
import socket


# Создание соединения
class Connection(object):
    destination = []
    port = 9595

    def __init__(self):
        self.sock = socket.socket()
        # self.data = data


    # Слушаем сокет
    def listen(self):
        self.sock.bind(('', self.port))
        self.sock(2)
        conn, addr = self.sock.accept()
        data = conn.recv(1024).decode()
        return data

    # Отправка данных
    def send(self, data, dest):
        with self.sock.connect((dest, self.port)):
            self.sock.send(data.encode())


# Действия
class Action(object):
    # def __init__(self, conn):
    #     self.conn = conn

    @staticmethod
    def get_tc(conn):
        for idx in storage.all_idx(conn):
            Connection.destination.append(idx)
            # Connection.send(idx['TC_ip'])

    # Отправка значений конфига виртуальной машине
    @staticmethod
    def send_tc_ip(comm):
        for i in Connection.destination:
            Connection.send(comm, i['TC_ip'], i['VM_ip'])


conn = storage.connect('base.db')
storage.initialize(conn)

Action.get_tc(conn)
print(Connection.destination)
Action.send_tc_ip(comm)
