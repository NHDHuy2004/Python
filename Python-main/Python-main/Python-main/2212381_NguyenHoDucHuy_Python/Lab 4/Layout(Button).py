from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUi()  # Gọi phương thức đúng cách
    
    def initUi(self):  # Phải đặt phương thức này ngoài __init__
        self.parent.title("Button")
        self.style = Style()
        self.style.theme_use("default")
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)
        
        closeButton = Button(self, text="Close", command=self.parent.quit)  # Đóng ứng dụng khi nhấn Close
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)

# Khởi tạo cửa sổ
root = Tk()
root.geometry("300x200+300+300")
app = Example(root)
root.mainloop()
