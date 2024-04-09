# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:13:29 2024

@author: RUMEYSA
"""

import cv2
from matplotlib import pyplot as plt

image=cv2.imread("C:/Users/RUMEYSA/opencv_lessons/1/original__0_4898200.png",0)
#0 parametresigri tonlamaya donusturuyor


#pencere olusturmak#
#cv2.namedWindow("image1",cv2.WINDOW_AUTOSIZE)
#Wındow_normal yaptıgımız zaman resmi buyultup kucultebiliyoruz
#cv2.imshow("image1", image)

cv2.imshow("wheat", image)

plt.imshow(image, cmap="gray")
plt.show()





k=cv2.waitKey(0)


if k==27:
    print("ESC tusuna basıldı")
    
elif k==ord("q")    :
    print("q tusuna basıldı,resim kayıt edildi")
    cv2.imwrite("wheatgri.jpg", image)
#bu swkilde yaptıgımızda klasore wheatgri imagini ekliyor.



#cv2.destroyWindow("image")
cv2.destroyAllWindows()