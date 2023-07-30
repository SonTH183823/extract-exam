import cv2
import os
def detect_questions(file, column):
    img = cv2.imread(file + "/image_full.png", cv2.IMREAD_COLOR)
    image_cau = cv2.imread(file + "/cau.png", cv2.IMREAD_COLOR)
    os.mkdir(file+'/questions')
    list_cau = []

    for i in range(img.shape[0] - image_cau.shape[0]):
        for j in range(column - 15, column + 10):
            image_ = img[i:i + image_cau.shape[0], j:j + image_cau.shape[1], :]
            comparison = image_cau == image_
            equal_image = comparison.all()
            if equal_image:
                list_cau.append((i, j))
    for i in range(len(list_cau) - 1):
        image_detect = img[list_cau[i][0] - 40:list_cau[i + 1][0] - 5, list_cau[i][1] - 20:, :]
        if i < 9:
            cv2.imwrite(file+'/questions' + f"/cau0{i + 1}.png", image_detect)
        else:
            cv2.imwrite(file+'/questions' + f"/cau{i + 1}.png", image_detect)
    print(f"detect cau thanh cong!")
    return "Cắt câu hỏi thành công!"
