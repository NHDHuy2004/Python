from tkinter.ttk import Frame, Label
from tkinter import Tk, BOTH, Listbox, StringVar, END

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Listbox")
        self.pack(fill=BOTH, expand=True)
  
        acts = ["Scarlett Johansson", "Rachel Weisz", "Natalie Portman", "Jessica Alba"]
  
        self.lb = Listbox(self)
  
        for i in acts:
            self.lb.insert(END, i)
  
        self.lb.bind("<<ListboxSelect>>", self.onSelect)
  
        self.lb.pack(pady=15)
  
        self.var = StringVar(value="")  # Khởi tạo với chuỗi rỗng
        self.label = Label(self, textvariable=self.var)  # Không cần text=0
        self.label.pack()

    def onSelect(self, event):
        sender = event.widget
        idx = sender.curselection()
        if idx:  # Kiểm tra xem có phần tử nào được chọn không
            value = sender.get(idx[0])  # Lấy phần tử đầu tiên trong tuple
            self.var.set(value)

root = Tk()
ex = Example(root)
root.geometry("300x250+300+300")
root.mainloop()
