import matplotlib.pyplot as plt
import cv2

#ภาพเป็นแบบ Gray (เทา)
gray_img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/32.png")

#thresh ค่าจุดแบ่ง                      #128 ค่าจุดแบ่ง 255ค่า Max
#ถ้าค่าสูงกว่าค่าจุดแบ่งจะเปลี่ยนเป็น 255 ที่เหลือเป็น 0
thresh1,th1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
#ถ้าค่าสูงกว่าค่าจุดแบ่งจะเปลี่ยนเป็น 0 ที่เหลือเป็น 255
thresh2,th2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
#ถ้าค่าสูงกว่าต่าจุดแบ่งจะเปลี่ยนให้มีค่าเท่ากับค่าจุดแบ่งที่เหลือมีค่าเท่าเดิม
thresh3,th3 = cv2.threshold(gray_img,50,255,cv2.THRESH_TRUNC)
#ถ้าค่าต่ำกว่าค่าจุดแบ่งจะเปลี่ยนเป็น 0 ที่เหลือคงเดิม
thresh4,th4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
#ถ้าค่าสูงกว่าค่าจุดแบ่งจะเปลี่ยนเป็น 0 ที่เหลือคงเดิม
thresh5,th5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)

#print(thresh1)

# cv2.imshow("Orignal",gray_img)
# cv2.imshow("BINARY",th1)
# cv2.imshow("BINARY_INV",th2)
# cv2.imshow("TRUNC",th3)
# cv2.imshow("TOZERO",th4)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

images = [gray_img,th1,th2,th3,th4,th5]
titles = ["ORIGINAL","BINARY","BINARY_INV","TRUNC","TOZERO","TOZERO_INV"]

for i in range(len(images)):
    plt.subplot(2,3,i+1) #2แถว 3คอลัม ตำแหน่งที่จะเอาภาพไปใส่
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) #ลบ x y แต่ละภาพ

plt.show()