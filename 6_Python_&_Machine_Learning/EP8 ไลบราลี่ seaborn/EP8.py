'''
Seaborn เป็นไลบรารีที่ใช้ Matplotlib ด้านล่างเพื่อพล็อตกราฟ มันจะถูกใช้เพื่อให้เห็นภาพการแจกแจงแบบสุ่ม
https://expert-programming-tutor.com/tutorial/article/L97_PYTHON_SEABORN.php
'''
import seaborn as sb
import matplotlib.pyplot as plt
iris_dataset=sb.load_dataset('iris')
print(iris_dataset.head())
sb.set()
sb.pairplot(iris_dataset,hue='species',size=2)#hue='species'= แบ่งสีให้แต่ละคอลัม /'species' คือชื่อคอลัม
plt.show()