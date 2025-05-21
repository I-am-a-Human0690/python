import cv2

a = 0
for i in range(10):
    if cv2.waitKey(10000) & a==1:
    #if cv2.waitKey(0) & a==1:
        print('e')
    print('test')

