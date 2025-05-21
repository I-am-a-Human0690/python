#Laplacian Method 
import cv2 

img = cv2.imread("Python/8_Python_&_OpenCV_Image_Processing/50.jpg",0)

lap = cv2.Laplacian(img,-1)

cv2.imshow("Original",img)
cv2.imshow("Laplacian",lap)

cv2.waitKey(0)
cv2.destroyAllWindows()