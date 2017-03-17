import sqlite3

SQL_SELECT = '''SELECT id, NetBIOS_TC, TC_ip, VM_ip FROM manager'''


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
                NetBIOS_TC TEXT NOT NULL DEFAULT '',
                TC_ip TEXT NOT NULL DEFAULT '',
                VM_ip TEXT NOT NULL DEFAULT ''
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


def add_comm(conn, netbios_tc, tc_ip):
    with conn:
        cursor = conn.execute('''
            INSERT INTO manager (NetBIOS_TC, TC_ip) VALUES (?,?)
        ''', (netbios_tc, tc_ip))


def find_by_id(conn, idx):
    with conn:
        cursor = conn.execute(SQL_SELECT + ''' WHERE id=?''', (idx,))
        return cursor.fetchone()


def all_idx(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT)
        return cursor.fetchall()