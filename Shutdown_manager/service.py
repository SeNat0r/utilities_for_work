from manager import storage
import socket
import pickle
from time import sleep


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
                    elif pi_data[1] == 'info':
                        self.add_comm(pi_data)
                elif pi_data[0] == 'client':
                    if pi_data[1] == 'check':
                        self.connect_check()
                    elif pi_data[1] == 'info':
                        self.add_vm(pi_data)
                elif pi_data[0] == 'gui':
                    if pi_data[1] == 'all_base':
                        self.return_db()
                    elif pi_data[1] == 'req_info':
                        self.return_info(pi_data[2])
                    elif pi_data[1] == 'edit_vm':
                        self.bind_vm(pi_data[2], pi_data[3])
                    elif pi_data[1] == 'get_vms':
                        self.get_vms()
            sleep(0.3)

    def connect_check(self):
        self.sock.send('666', self.sock.addres)

    def add_comm(self, d):
        storage.add_communication(self.db, d[2], self.sock.addres, d[3])

    def return_db(self):
        d = storage.all_data(self.db)
        self.sock.send(d, self.sock.addres)

    def return_info(self, selected):
        info = storage.find_by_name(self.db, selected)
        self.sock.send(info, self.sock.addres)

    def bind_vm(self, thinclient, vm):
        storage.update_binding(self.db, thinclient, vm)

    def get_vms(self):
        vms = storage.all_vms(self.db)
        self.sock.send(vms, self.sock.addres)

    def add_vm(self, d):
        storage.add_vm(self.db, d[2], self.sock.addres)






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
storage.init_vms_db(conn)

s = Socket(9696)
b = Server(s, conn)
b.listen()
