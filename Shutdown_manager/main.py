from manager import storage
import socket


# Создание соединения
class Socket(object):
    def __init__(self, port):
        self.__sock = socket.socket()
        self.port = port

    def listen(self):
        """Прослушка сокета"""
        self.__sock.bind(('', self.port))
        self.__sock.listen(2)
        conn, addr = self.__sock.accept()
        data = conn.recv(1024).decode()
        return data

    def send(self, data, conn):
        """Отправка данных"""
        self.__sock.connect((conn, self.port))
        self.__sock.send(data.encode())
        self.__sock.close()


# Действия
class Manager(object):
    def __init__(self):
        self.manager_key = '666'

    @staticmethod
    def get_tc(conn):
        for idx in storage.all_idx(conn):
            Socket.destination.append(idx)
            # Connection.send(idx['TC_ip'])

    # Отправка значений конфига виртуальной машине
    @staticmethod
    def send_tc_ip(comm):
        for i in Socket.destination:
            Socket.send(comm, i['TC_ip'], i['VM_ip'])

#
# conn = storage.connect('base.db')
# storage.initialize(conn)

s = Socket(9595)
m = Manager()
while True:
    data = s.listen()
    print(data)
    if data['type'] == 'server' and data['check']:
        s.send(m.manager_key)


