import sqlite3

SQL_SELECT = '''SELECT id, host_name, tc_ip, vm_ip, vm_name, action_key FROM manager'''
SQL_SELECT_VMS = '''SELECT id, vm_name, ip FROM vms'''


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Инициализация базы
def initialize(conn):
    with conn:
        cursor = conn.executescript('''
            CREATE TABLE IF NOT EXISTS manager (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                host_name TEXT NOT NULL DEFAULT '',
                tc_ip TEXT NOT NULL DEFAULT '',
                vm_ip TEXT NOT NULL DEFAULT '',
                action_key TEXT NOT NULL DEFAULT '',
                vm_name TEXT NOT NULL DEFAULT '',
                up INTEGER NOT NULL DEFAULT ''
            )
        ''')


def init_vms_db(conn):
    with conn:
        cursor = conn.executescript('''
            CREATE TABLE IF NOT EXISTS vms (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                vm_name TEXT NOT NULL DEFAULT '',
                ip TEXT NOT NULL DEFAULT ''
            )
        ''')


# Подключение(создание) к базе данных
def connect(db_name=None):
    # Если название базы не указано, загружать базу в ОЗУ
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn


def add_communication(conn, name_tc, tc_ip, action_key):
    with conn:
        cursor = conn.execute(SQL_SELECT + ''' WHERE host_name=?''', (name_tc,))
        if cursor.fetchone():
            cursor = conn.execute('''
                            UPDATE manager SET tc_ip=?, action_key=? WHERE host_name=?
                        ''', (tc_ip, action_key, name_tc))
        else:
            cursor = conn.execute('''
                INSERT INTO manager (host_name, tc_ip, action_key) VALUES (?,?,?)
            ''', (name_tc, tc_ip, action_key))


def add_vm(conn, vm_name, ip):
    with conn:
        cursor = conn.execute(SQL_SELECT_VMS + ''' WHERE vm_name=?''', (vm_name,))
        if cursor.fetchone():
            cursor = conn.execute('''
                            UPDATE vms SET ip=? WHERE vm_name=?
                        ''', (ip, vm_name))
        else:
            cursor = conn.execute('''
                INSERT INTO vms (vm_name, ip) VALUES (?,?)
            ''', (vm_name, ip))

def find_by_name(conn, host_name):
    with conn:
        cursor = conn.execute(SQL_SELECT + ''' WHERE host_name=?''', (host_name,))
        return cursor.fetchone()


def find_by_vmname(conn, vm_name):
    with conn:
        cursor = conn.execute(SQL_SELECT_VMS + ''' WHERE vm_name=?''', (vm_name,))
        return cursor.fetchone()

def all_data(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT)
        return cursor.fetchall()


def all_vms(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_VMS)
        temp = cursor.fetchall()
        vms = []
        for d in temp:
            vms.append(d['vm_name'])
        return vms



def update_binding(conn, name_tc, vm_name):
    vm_ip = find_by_vmname(conn, vm_name)
    with conn:
        cursor = conn.execute('''
            UPDATE manager SET vm_name=?, vm_ip=? WHERE host_name=?
        ''', (vm_name, vm_ip['ip'], name_tc))
