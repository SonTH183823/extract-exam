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
    folder = os.path.dirname(file)
    locfile = os.path.basename(file)
    file_name = os.path.splitext(locfile)[0]
    image_full_text_done.configure(text="B1: Đang thực hiện...")
    container_folder = folder + '/' + file_name
    doneCutted = pdftoimage.create_image(file=file, folder=container_folder)
    image_full_text_done.configure(text="B1:" + str(doneCutted))
    image_full_text_done1.configure(text="B2: Đang thực hiện...")
    for i in [8, 7, 6, 5]:
        try:
            doneImageFull = pdftoimage.create_image_full(num_pages=i, folder=container_folder)
            image_full_text_done1.configure(text="B2: " + str(doneImageFull))
            image_full_text_done2.configure(text="B3: Đang thực hiện...")
            column = extract_cau.extract_cau_(container_folder)
            done = detect.detect_cau(container_folder, column=column)
            image_full_text_done2.configure(text="B3: " + str(done))
            break
        except:
            continue


if __name__ == "__main__":
    def handleButton():
        file = filedialog.askopenfilename(**FILEOPENOPTIONS)
        process(file)
        return


    window = Tk()
    window.title("Cắt đề thi")
    window.geometry("500x300")

    nameProgram = tkinter.Label(window, text="Tiêu đề")
    nameProgram.config(font=("Arial", 30))
    nameProgram.pack(pady=10)
    btnChose = Button(window, text="Chọn file đề thi", command=handleButton)
    btnChose.place(x=100, y=70)
    image_full_text_done = tkinter.Label(window, text="")
    image_full_text_done.config(font=("Arial", 14))
    image_full_text_done.place(x=70, y=100)
    image_full_text_done1 = tkinter.Label(window, text="")
    image_full_text_done1.config(font=("Arial", 14))
    image_full_text_done1.place(x=70, y=130)
    image_full_text_done2 = tkinter.Label(window, text="")
    image_full_text_done2.config(font=("Arial", 14))
    image_full_text_done2.place(x=70, y=160)
    window.mainloop()
