import cv2
import numpy as np
import os

while True:
    text = input("Translator(rgb, gray, binary, hist): ")
    print(text)

    values=[1,2,3,4,5,6,7,8,9,10]
    
    #rgb->rgb
    if (text == "rgb"):
        # rgb to rgb
        for value in values:
            str_value = str(value) + ".jpg"
            path = "C:/Users/RUMEYSA/opencv_lessons/1/" + str_value
            image = cv2.imread(path)

            (row, col, p) = image.shape[0:3]
            blank_rgb_image = np.zeros((row, col, p), np.uint8)

            for k in range(p):
                for i in range(row):
                    for j in range(col):
                        blank_rgb_image[i, j, k] = image[i, j, k]

            for k in range(3):
                for i in range(225):
                    for j in range(225):
                        blank_rgb_image[i, j, k] = image[i, j, k]

            path1 = 'C:/Users/RUMEYSA/opencv_lessons/1/RGB/'
            cv2.imwrite(os.path.join(path1, str_value), blank_rgb_image)
     
     #rgb->gray
    elif (text == "gray"):
        # rgb to grayscale
        for value in values:
            str_value = str(value) + ".jpg"
            path = "C:/Users/RUMEYSA/opencv_lessons/1/" + str_value
            image = cv2.imread(path)

            (row, col) = image.shape[0:2]
            gray_image = np.zeros((row, col), np.uint8)

            for i in range(row):
                for j in range(col):
                    gray_image[i, j] = sum(image[i, j]) * 0.33

            path2 = 'C:/Users/RUMEYSA/opencv_lessons/1/GrayScale/'
            cv2.imwrite(os.path.join(path2, str_value), gray_image)
    
     #rgb->binary
    elif (text == "binary"):
        for value in values:
            str_value = str(value) + ".jpg"
            path = "C:/Users/RUMEYSA/opencv_lessons/1/" + str_value
            image = cv2.imread(path)
            # rgb to binary
            binary_gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            (row, col) = binary_gray_image.shape[0:2]

            for i in range(row):
                for j in range(col):
                    if binary_gray_image[i, j] > 87:
                        binary_gray_image[i, j] = 255
                    else:
                        binary_gray_image[i, j] = 0

            path3 = 'C:/Users/RUMEYSA/opencv_lessons/1/Binary/'
            cv2.imwrite(os.path.join(path3, str_value), binary_gray_image)

    
     #rgb->hist
    elif (text == "hist"):
        for value in values:
            str_value = str(value) + ".jpg"
            path = "C:/Users/RUMEYSA/opencv_lessons/1/" + str_value
            image = cv2.imread(path)
        # gray to histogram stretching
            hist_gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            a = [0, 50, 118, 225, 255]
            b = [10, 50, 150, 200, 255]


            def histpwl(hist_gray_image, a, b):
                # Check if input image is not of type double, convert if necessary
                classChanged = 0
                if hist_gray_image.dtype != np.float64:
                    classChanged = 1
                    hist_gray_image = hist_gray_image.astype(np.float64) / 255.0

                # Check if lengths of vectors a and b are equal
                if len(a) != len(b):
                    raise ValueError('Vectors A and B must be of equal size')

                N = len(a)
                out = np.zeros_like(hist_gray_image)

                for i in range(N - 1):
                    pix = np.where((hist_gray_image >= a[i]) & (hist_gray_image < a[i + 1]))
                    out[pix] = (hist_gray_image[pix] - a[i]) * (b[i + 1] - b[i]) / (a[i + 1] - a[i]) + b[i]

                pix = np.where(hist_gray_image == a[N - 1])
                out[pix] = b[N - 1]

                if classChanged == 1:
                    out = (out * 255).astype(np.uint8)

                return out


            result_image = histpwl(hist_gray_image, a, b)
            path4 = 'C:/Users/RUMEYSA/opencv_lessons/1/HisGer/'
            cv2.imwrite(os.path.join(path4, str_value), result_image)

    else:
        print("böyle bir dönüşüm yok")




