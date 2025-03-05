from tkinter import Tk, Frame, BOTH

class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent, background="white")
        self.initUI()

    def initUI(self):
        self.master.title("Simple")
        self.pack(fill=BOTH, expand=True)

if __name__ == "__main__":
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.master.title("Quit button")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=True)

        quit_button = Button(self, text="Quit", command=self.on_quit)
        quit_button.place(x=50, y=50)

    def on_quit(self):
        """Phương thức để thoát chương trình."""
        self.master.quit()

if __name__ == "__main__":
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()
