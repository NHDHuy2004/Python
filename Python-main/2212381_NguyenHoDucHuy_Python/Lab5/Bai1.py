import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=PC721;DATABASE=QLMonAn;UID=sa;PWD=sa;Encrypt=no')
cursor = conn.cursor()
cursor.execute("SELECT @@version")
conn.close()

db_version = cursor.fetchone()
print("Bạn đang dùng hệ quản trị CSDL SQL server phiên bản ", db_version)

import sqlite3

def get_connection():
    connection = sqlite3.connect('QLSinhVien.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select sqlite_version();")
        db_version = cursor.fetchone()
        print("Bạn đang sử dụng SQLite phiên bản: ", db_version)
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ", error)

read_database_version()

import pyodbc

connectionString = '''DRIVER={ODBC Driver 18 for SQL Server};
                      SERVER=PC721;DATABASE=QLSinhVien;UID=sa;PWD=sa;Encrypt=no'''

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from Lop"""
        cursor.execute(select_query)

        records = cursor.fetchall()

        print(f"Danh sách các lớp là: ")
        print("*" * 50)
        for row in records:
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

get_all_class()
