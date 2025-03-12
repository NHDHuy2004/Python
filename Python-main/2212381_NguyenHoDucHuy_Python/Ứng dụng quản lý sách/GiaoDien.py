# Lưu trữ thông tin sách trong một danh sách
book_collection = []

def add_book(book_id, title, author, release_date, genre):
    book = {
        'id': book_id,
        'title': title,
        'author': author,
        'release_date': release_date,
        'genre': genre
    }
    book_collection.append(book)

def search_books(keyword):
    result = [book for book in book_collection if keyword.lower() in book['title'].lower() or 
                                                  keyword.lower() in book['author'].lower() or
                                                  keyword.lower() in book['genre'].lower()]
    return result

#Giao diện người dùng
import tkinter as tk
from tkinter import messagebox

def add_book_gui():
    book_id = id_entry.get()
    title = title_entry.get()
    author = author_entry.get()
    release_date = release_date_entry.get()
    genre = genre_entry.get()
    add_book(book_id, title, author, release_date, genre)
    messagebox.showinfo("Thông báo", "Sách đã được thêm thành công!")

root = tk.Tk()
root.title("Quản lý Sách Điện Tử")

tk.Label(root, text="ID sách").grid(row=0)
tk.Label(root, text="Tiêu đề").grid(row=1)
tk.Label(root, text="Tác giả").grid(row=2)
tk.Label(root, text="Ngày phát hành").grid(row=3)
tk.Label(root, text="Thể loại").grid(row=4)

id_entry = tk.Entry(root)
title_entry = tk.Entry(root)
author_entry = tk.Entry(root)
release_date_entry = tk.Entry(root)
genre_entry = tk.Entry(root)

id_entry.grid(row=0, column=1)
title_entry.grid(row=1, column=1)
author_entry.grid(row=2, column=1)
release_date_entry.grid(row=3, column=1)
genre_entry.grid(row=4, column=1)

tk.Button(root, text='Thêm sách', command=add_book_gui).grid(row=5, column=0, columnspan=2)

root.mainloop()

#Tìm kiếm sách
def search_books(keyword):
    result = [book for book in book_collection if keyword.lower() in book['title'].lower() or 
                                                keyword.lower() in book['author'].lower() or
                                                keyword.lower() in book['genre'].lower()]
    return result

#Thêm sách mới
def add_book(book_id, title, author, release_date, genre):
    book = {
        'id': book_id,
        'title': title,
        'author': author,
        'release_date': release_date,
        'genre': genre
    }
    book_collection.append(book)

#Lưu trữ thông tin sách
book_collection = []

def add_book(book):
    book_collection.append(book)
