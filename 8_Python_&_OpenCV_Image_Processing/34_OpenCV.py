#เทียบค่า Threshold ด้วย Matplotlib
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/34.jpg")

#ภาพเป็นแบบสี Gray (เทา)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#ค่าตัวแบ่ง
thresh_value = [50,100,130,200,230]

plt.subplot(231,xticks=[],yticks=[]) #2แถว 3คอลัม ตำแหน่งที่จะเอาภาพไปใส่ #ลบ x y แต่ละภาพ
plt.title("Original")
plt.imshow(gray_img,cmap="gray")

for i in range(len(thresh_value)):
    #thresh เก็บค่าจุดแบ่ง                      #i ค่าจุดแบ่ง 255ค่า Max
    #THRESH_BINARY อื่นๆอยู่ที่#33 ถ้าค่าสูงกว่าค่าจุดแบ่งจะเปลี่ยนเป็น 255 ที่เหลือเป็น 0
    thresh,result = cv2.threshold(gray_img,thresh_value[i],255,cv2.THRESH_BINARY)
    plt.subplot(232+i)
    plt.title("%d"%thresh_value[i])
    plt.imshow(result,cmap="gray")#cmap="gray" ทำให้ภาพเป็นสีเทา
    plt.xticks([]),plt.yticks([])

plt.show()