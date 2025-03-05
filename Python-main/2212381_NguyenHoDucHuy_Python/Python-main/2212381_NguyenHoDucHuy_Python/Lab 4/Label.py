from PIL import Image, ImageTk
from tkinter import Tk, Frame, Label
import os

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Label")

        # Kiểm tra xem ảnh có tồn tại không
        image_path = r"D:\download.jpg"
        if not os.path.exists(image_path):
            print(f"Error: File not found at {image_path}")
            return  # Dừng nếu không tìm thấy ảnh

        self.img = Image.open(image_path)
        rotunda = ImageTk.PhotoImage(self.img)
        label = Label(self, image=rotunda)
        label.image = rotunda
        label.pack()
        self.pack()

        self.setGeometry()  # Gọi setGeometry() sau khi ảnh được load thành công

    def setGeometry(self):
        w, h = self.img.size
        self.parent.geometry(f"{w}x{h}+300+300")

root = Tk()
ex = Example(root)
root.mainloop()
