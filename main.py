import pdftoimage
import detect
import extract_cau
import argparse
# Tạo đường dẫn tới poppler

# ui
from tkinter import *
from tkinter.ttk import *
import tkinter
from tkinter import filedialog


def parse_args():
    parser = argparse.ArgumentParser(description='detect ex')
    parser.add_argument('-f', '--file', help='file pdf input')
    parser.add_argument('-pp', '--poppler_path', default="./poppler-21.09.0/bin", help='file pdf input')
    args = parser.parse_args()
    return args

FILEOPENOPTIONS = dict(defaultextension=".pdf",filetypes=[('pdf file', '*.pdf')])

def process(file):
    pdftoimage.creat_image(file=file)
    # for i in [8, 7, 6, 5]:
    #     try:
    #         pdftoimage.creat_image_full(file=file, num_pages=i)
    #         # y1, y2,
    #         column = extract_cau.extract_cau_(file)
    #         detect.detect_cau(file, column=column)
    #         break
    #     except:
    #         continue

if __name__ == "__main__":
    def handleButton():
        file = filedialog.askopenfilename(**FILEOPENOPTIONS)
        print('aloooo', file)
        process(file)
        return


    window = Tk()
    window.title("Cắt đề thi")
    window.geometry("600x400")

    nameProgram = tkinter.Label(window, text="Tiêu đề")
    nameProgram.config(font=("Arial", 30))
    nameProgram.pack(pady=10)
    btnChose = Button(window, text="Chọn ảnh", command=handleButton)
    btnChose.place(x=150, y=200)
    window.mainloop()
    # args = parse_args()
    # print("aloooooooo", args)
    # file = args.file
    # poppler_path = args.poppler_path

