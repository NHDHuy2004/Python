import tkinter as tk
from tkinter import messagebox, simpledialog

# Lưu trữ thông tin sách
book_collection = []

# Thêm sách mới vào danh sách
def add_book(book_id, title, author, release_date, genre):
    book = {
        'id': book_id,
        'title': title,
        'author': author,
        'release_date': release_date,
        'genre': genre
    }
    book_collection.append(book)

# Tìm kiếm sách theo từ khóa
def search_books(keyword):
    result = [book for book in book_collection if keyword.lower() in book['title'].lower() or
                                                keyword.lower() in book['author'].lower() or
                                                keyword.lower() in book['genre'].lower()]
    return result

# Giao diện người dùng
def add_book_gui():
    book_id = id_entry.get()
    title = title_entry.get()
    author = author_entry.get()
    release_date = release_date_entry.get()
    genre = genre_entry.get()

    if not all([book_id, title, author, release_date, genre]):
        messagebox.showwarning("Cảnh báo", "Vui lòng điền đầy đủ thông tin!")
        return

    add_book(book_id, title, author, release_date, genre)
    messagebox.showinfo("Thông báo", "Sách đã được thêm thành công!")
    id_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    release_date_entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)

def search_books_gui():
    keyword = simpledialog.askstring("Tìm kiếm sách", "Nhập từ khóa tìm kiếm:")
    if not keyword:
        return

    results = search_books(keyword)
    if results:
        result_text = "\n".join([f"ID: {book['id']}, Tiêu đề: {book['title']}, Tác giả: {book['author']}" for book in results])
        messagebox.showinfo("Kết quả tìm kiếm", result_text)
    else:
        messagebox.showinfo("Kết quả tìm kiếm", "Không tìm thấy sách nào phù hợp.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý Sách Điện Tử")

# Các nhãn và ô nhập liệu
tk.Label(root, text="ID sách").grid(row=0, column=0)
tk.Label(root, text="Tiêu đề").grid(row=1, column=0)
tk.Label(root, text="Tác giả").grid(row=2, column=0)
tk.Label(root, text="Ngày phát hành").grid(row=3, column=0)
tk.Label(root, text="Thể loại").grid(row=4, column=0)

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

# Các nút
tk.Button(root, text='Thêm sách', command=add_book_gui).grid(row=5, column=0, columnspan=2)
tk.Button(root, text='Tìm kiếm sách', command=search_books_gui).grid(row=6, column=0, columnspan=2)

root.mainloop()
