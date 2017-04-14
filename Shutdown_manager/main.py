from manager import storage
import socket


# Создание соединения
class Socket(object):
    def __init__(self, port):
        self.destination = ('127.0.0.1', port)

    # Биндим интерфейс, порт
    # Слушаем макс 2 соединения
    # получаем и декодируем пакеты по 1024 байта
    def listen(self):
        """Прослушка сокета"""
        with socket.socket() as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(self.destination)
            s.listen(2)

            while True:
                conn, adr = s.accept()

                with conn:
                    data = conn.recv(1024).decode()
                    if data:
                        print(data)
                        return data

    def send(self, data):
        """Отправка данных"""
        with socket.socket() as s:
            s.connect(self.destination)
            s.send(data.encode())


# Действия
class Manager(object):
    def __init__(self):
        self.manager_key = '666'

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
s.send('atata')