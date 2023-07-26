import pdftoimage
import detect
import extract_cau
import os

# ui
from tkinter import *
from tkinter.ttk import *
import tkinter
from tkinter import filedialog

FILEOPENOPTIONS = dict(defaultextension=".pdf", filetypes=[('pdf file', '*.pdf')])


def process(file):
    image_full_text_done1.configure(text="File: " + file)
    image_full_text_done.configure(text="B1: Đang thực hiện cắt ảnh...")
    folder = os.path.dirname(file)
    locfile = os.path.basename(file)
    file_name = os.path.splitext(locfile)[0]
    container_folder = folder + '/' + file_name
    progress['value'] = 20
    window.update_idletasks()
    pdftoimage.create_image(file=file, folder=container_folder)
    image_full_text_done.configure(text="B2: Đang thực hiện tạo ảnh full...")
    progress['value'] = 40
    window.update_idletasks()
    for i in [8, 7, 6, 5]:
        try:
            pdftoimage.create_image_full(num_pages=i, folder=container_folder)
            image_full_text_done.configure(text="B3: Đang thực hiện tách câu hỏi")
            progress['value'] = 60
            window.update_idletasks()
            # image_full_text_done1.configure(text="B2: " + str(doneImageFull))
            # image_full_text_done2.configure(text="B3: Đang thực hiện...")
            column = extract_cau.extract_cau_(container_folder)
            progress['value'] = 80
            window.update_idletasks()
            done = detect.detect_cau(container_folder, column=column)
            progress['value'] = 100
            window.update_idletasks()
            image_full_text_done.configure(text="Hoàn thành")
            break
        except:
            continue


if __name__ == "__main__":
    def handleButton():
        image_full_text_done1.configure(text="File: chưa chọn" )
        progress['value'] = 0
        window.update_idletasks()
        file = filedialog.askopenfilename(**FILEOPENOPTIONS)
        if file:
            process(file)
        return


    window = Tk()
    window.title("Cắt đề thi")
    window.geometry("500x250")

    nameProgram = tkinter.Label(window, text="Cắt đề thi")
    nameProgram.config(font=("Arial", 30))
    nameProgram.pack(pady=10)
    btnChose = Button(window, text="Chọn file đề thi", command=handleButton)
    btnChose.place(x=30, y=70)
    progress = Progressbar(window, orient=HORIZONTAL, length=400, mode='determinate')
    progress.place(x=30, y=170)
    image_full_text_done = tkinter.Label(window, text="Tiến trình")
    image_full_text_done.config(font=("Arial", 14))
    image_full_text_done.place(x=30, y=140)
    image_full_text_done1 = tkinter.Label(window, text="File: chưa chọn")
    image_full_text_done1.config(font=("Arial", 14))
    image_full_text_done1.place(x=30, y=110)
    window.mainloop()
