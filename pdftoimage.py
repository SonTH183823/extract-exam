from pdf2image import convert_from_path
import os
import cv2


def del_last_page(img):
    line_white = img[-1, :, :]
    line = img.shape[0] - 1
    while True:
        comparison = line_white == img[line, :, :]
        equal_image = comparison.all()
        if equal_image == False:
            while True:
                comparison1 = line_white == img[line, :, :]
                equal_image1 = comparison1.all()
                if equal_image1 == True:
                    line_h = line
                    return line_h - 10
                line -= 1
        line -= 1


def create_image(file, folder, poppler_path=''):
    pages = convert_from_path(file, 500)
    try:
        os.mkdir(folder)
    except:
        print("loi tao thu muc")

    num_image = 1
    for page in pages:
        page.save(folder + f'/page{num_image}.png', 'PNG')
        num_image += 1
    return "Cắt ảnh từ file fpd thành công!"


def create_image_full(num_pages, folder):
    image = []
    for i in range(1, num_pages + 1):
        img = cv2.imread(folder + f"/page{i}.png", cv2.IMREAD_COLOR)
        line_h = del_last_page(img)
        img = img[:line_h, :, :]
        cv2.imwrite(folder + f"/page{i}_cutted.png", img)
        image.append(img)
    for i in range(1, num_pages):
        image[0] = cv2.vconcat([image[0], image[i]])
    cv2.imwrite(folder + "/image_full.png", image[0])
    print("da tao thanh cong image_full de thi")
    return "Tạo thành công image_full từ các file ảnh đã cắt"
