import sqlite3
from config import *


def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    result = cursor.fetchall()
    connection.close()
    return result


get_all_products()


def add_values():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products(id, title, description, price) VALUES (?,?,?,?)',
                       (f'{i}', f'{product_list[i - 1]}', f'{descriptions_list[i - 1]}', i * 100))
    connection.commit()
    connection.close()
