import sqlite3


# Инициализация базы
def initialize(conn):
    with conn:
        cursor = conn.executescript('''
            CREATE TABLE IF NOT EXISTS manager (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                DN TEXT NOT NULL DEFAULT '',
                VM TEXT NOT NULL DEFAULT '',
                ThinMachine TEXT NOT NULL DEFAULT ''
            )
        ''')


# Подключение(создание) к базе данных
def connect(db_name=None):
    # Если название базы не указано, загружать базу в ОЗУ
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    # conn.row_factory = dict_factory

    return conn


def add_task(conn, task_name, task_date, text):
    with conn:
        cursor = conn.execute('''
            INSERT INTO scheluder (task_name, task_date, text) VALUES (?,?,?)
        ''', (task_name, task_date, text))