from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style

class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)  # Sử dụng super() thay vì gọi trực tiếp Frame.__init__
        self.parent = parent
        self.initUI()  # Đảm bảo phương thức được gọi đúng

    def initUI(self):  # Đảm bảo tên đúng "initUI"
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        bard = Image.open("D:\download (1).jpg")
        bard = bard.resize((100, 100), Image.LANCZOS)  # Thay Image.ANTIALIAS bằng Image.LANCZOS
        bardejov = ImageTk.PhotoImage(bard)

        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)

        rot = Image.open("D:\download.jpg")
        rot = rot.resize((100, 100), Image.LANCZOS)
        rotunda = ImageTk.PhotoImage(rot)

        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)

        minc = Image.open("D:\download (2).jpg")
        minc = minc.resize((100, 100), Image.LANCZOS)
        mincol = ImageTk.PhotoImage(minc)

        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)

if __name__ == "__main__":
    root = Tk()
    root.geometry("300x280+300+300")
    app = Example(root)  # Không còn lỗi "initUI không tồn tại"
    root.mainloop()
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
        def initUI(self):
            self.parent.title("Button")
            self.style = Style()
            self.style.theme_use("default")
            
            frame = Frame(self, relief=RAISED, borderwidth=1)
            frame.pack(fill=BOTH, expand=True)
            self.pack(fill=BOTH, expand=True)
            
            closeButton = Button(self, text="Close")
            closeButton.pack(side=RIGHT, padx=5, pady=5)
            okButton = Button(self, text="OK")
            okButton.pack(side=RIGHT)

root = Tk()
root.geometry("300x200+300+300")
app = Example(root)
root.mainloop()
