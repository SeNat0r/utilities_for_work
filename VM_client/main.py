import socket
import configparser


# def manager_edit(addr):
#     config = configparser.RawConfigParser()
#     config.read('default.ini')
#     config.set('DEFAULT', 'manager', addr)
#     with open('default.ini', 'w') as configfile:
#         config.write(configfile)
#
#
# def tm_edit(addr):
#     config = configparser.RawConfigParser()
#     config.read('default.ini')
#     config.set('DEFAULT', 'thin_client', addr)
#     with open('default.ini', 'w') as configfile:
#         config.write(configfile)
#
#
# def config_init():
#     config = configparser.RawConfigParser()
#     config.read('default.ini')
#     manager = config.get('DEFAULT', 'manager')
#     tm = config.get('DEFAULT', 'thin_client')
#     return manager, tm
#
#
# manager, thin = config_init()
#
# connect(thin)

# Создание соединения
class Connection(object):
    def __init__(self, port):
        self.__sock = socket.socket()
        self.port = port

    # Биндим интерфейс, порт
    # Слушаем макс 2 соединения
    # получаем и декодируем пакеты по 1024 байта
    def do_listen(self):
        """Прослушка сокета"""
        self.__sock.bind(('', self.port))
        self.__sock.listen(2)
        conn, addr = self.__sock.accept()
        data = conn.recv(1024).decode()
        return data

    # Устанавливаем соединение (адрес, порт)
    # Кодируем и посылаем данные
    # Закрываем соединение
    def send(self, data):
        """Отправка данных"""
        self.__sock.connect((self.destination, self.port))
        self.__sock.send(data.encode())
        self.__sock.close()


# Работа с конфигом
class Config(object):
    # def __init__(self, addr):
    #     self.addr = addr

    @staticmethod
    def get_config():
        """Получение значений конфигураций из ini файла"""
        config = configparser.RawConfigParser()
        config.read('default.ini')
        manager = config.get('DEFAULT', 'manager')
        tc = config.get('DEFAULT', 'thin_client')
        # return manager, tc
        return tc

        # def edit_config_tc(self):
        #     config = configparser.RawConfigParser()
        #     config.read('default.ini')
        #     config.set('DEFAULT', 'thin_client', self.addr)
        #     with open('default.ini', 'w') as configfile:
        #         config.write(configfile)


class Action(object):
    @staticmethod
    def start(port):
        """Отправка команды на удаленный сервер"""
        cmd = input()
        addr = Config.get_config()
        c = Connection(port, addr)


Action.start(9596)