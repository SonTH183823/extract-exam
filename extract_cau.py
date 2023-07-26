import cv2

def check_cau(image_cau, img, column):
    list_cau = []

    for i in range(img.shape[0] - image_cau.shape[0]):
        for j in range(column - 15, column + 10):
            image_ = img[i:i + image_cau.shape[0], j:j + image_cau.shape[1], :]
            comparison = image_cau == image_
            equal_image = comparison.all()
            if equal_image:
                list_cau.append((i, j))
    if len(list_cau) >= 4:
        return True
    else:
        return False


def extract_cau_(file):
    img = cv2.imread(file + "/page1_cutted.png", cv2.IMREAD_COLOR)
    h, w, c = img.shape
    column_white = img[h * 3 // 4:, 0, :]
    column = 0
    while True:
        comparison = column_white == img[h * 3 // 4:, column, :]
        equal_image = comparison.all()
        if equal_image == False:
            img_column = img[h * 3 // 4:, column, :]
            line = img_column.shape[0] - 1
            while True:
                comparison1 = img_column[-1, :] == img_column[line, :]
                equal_image1 = comparison1.all()
                if equal_image1 == False:
                    # img_____ = img[:h-line,column:,:]
                    # cv2.imwrite(file+"/xxxxx.png", img_____)
                    img_cau = img[h - img_column.shape[0] + line - 40:h - img_column.shape[0] + line + 30,
                              column - 10:column + 150, :]
                    if check_cau(img_cau, img, column):
                        cv2.imwrite(file + "/cau.png", img_cau)
                        return column
                line -= 1
                if line < 50:
                    break
        column += 1


