import cv2

img = cv2.imread('Python/8_Python_&_OpenCV_Image_Processing/2_OpenCV/test.png')

#รูปเก็บ ประกอบไปด้วยจุดสี
print(img)

#เช็คมิติภาพ
print(img.ndim)

#เช็คtype
print(type(img.ndim))