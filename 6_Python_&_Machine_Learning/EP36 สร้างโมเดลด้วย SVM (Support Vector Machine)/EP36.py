#ต่อจาก EP35
'''
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-8-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%94%E0%B8%88%E0%B8%B3%E0%B9%83%E0%B8%9A%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2-face-recognition-f7ec4629217c
สรุป Machine Learning(EP.8) — การจดจำใบหน้า (Face Recognition)
pip install -U scikit-learn
'''
'''
https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
whiten ค่าเริ่มต้น=False
เมื่อ True (False โดยค่าเริ่มต้น) components_เวกเตอร์จะถูกคูณด้วยสแควร์รูทของ n_samples 
แล้วหารด้วยค่าเอกพจน์เพื่อให้แน่ใจว่าเอาต์พุตที่ไม่สัมพันธ์กันกับความแปรปรวนตามองค์ประกอบหน่วย
ไวท์เทนนิ่งจะลบข้อมูลบางส่วนออกจากสัญญาณที่แปลงแล้ว (มาตราส่วนความแปรปรวนสัมพัทธ์ของส่วนประกอบ) 
แต่บางครั้งสามารถปรับปรุงความแม่นยำในการคาดการณ์ของตัวประมาณค่าดาวน์สตรีมได้ด้วยการทำให้ข้อมูลเป็นไปตามสมมติฐานแบบมีสาย

svd_solver {'auto', 'full', 'arpack', 'randomized'}, default='auto'
ถ้าอัตโนมัติ :
ตัวแก้ไขถูกเลือกโดยนโยบายเริ่มต้นตามX.shapeและ n_components: หากข้อมูลที่ป้อนเข้ามีขนาดใหญ่กว่า 500x500 
และจำนวนส่วนประกอบที่จะแยกต่ำกว่า 80% ของมิติข้อมูลที่เล็กที่สุด วิธีการ 'สุ่ม' ที่มีประสิทธิภาพมากขึ้นจะเปิดใช้งาน . มิฉะนั้น 
ระบบจะคำนวณ SVD แบบเต็มที่แน่นอนและตัดทอนในภายหลัง
'''
'''
https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
sklearn.svm.SVC
class_weight dict หรือ 'balanced' ค่าเริ่มต้น=ไม่มี
ตั้งค่าพารามิเตอร์ C ของคลาส i เป็น class_weight[i]*C สำหรับ SVC ถ้าไม่ได้รับ
 ทุกคลาสควรจะมีน้ำหนักหนึ่ง โหมด "สมดุล" ใช้ค่าของ y เพื่อปรับน้ำหนักโดยอัตโนมัติตามสัดส่วนผกผันกับความถี่ของคลาสในข้อมูลที่ป้อนเป็น
 n_samples / (n_classes * np.bincount(y))
'''
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sb

#download & display image
faces=fetch_lfw_people(min_faces_per_person=60)#min_faces_per_person=60 ข้อมูลใบหน้าของแต่ละคน 60 แบบ

# print(faces .target_names) #ชื่อเจ้าของใบหน้า
# print(faces.images.shape)
# # fig,ax=plt.subplots(3,5)
# for i ,axi in enumerate(ax.flat):
#     axi.imshow(faces.images[i],cmap='bone')
#     axi.set(xticks=[],yticks=[])
#     axi.set_ylabel(faces.target_names[faces.target[i]].split()[-1],color='black')
# plt.show()

#reduce(ลดขนาด) & create model
pca=PCA(n_components=150,svd_solver="randomized",whiten=True)#กำหนด n_components=150 ลดให้เหลือ 150 แค่กำหนด
svc=SVC(kernel='rbf',class_weight="balanced")

model=make_pipeline(pca,svc)
#sklearn.pipeline.make_pipeline(*steps, memory=None, verbose=False)( * ขั้นตอน ,หน่วยความจำ= ไม่มี ,ละเอียด= เท็จ )

#train , test data
x_train,x_test,y_train,y_test=train_test_split(faces.data,faces.target,random_state=40)
param={'svc__C':[1,5,10,50],'svc__gamma':[0.0001,0.0005,0.001,0.005]}
'''
การปรับค่าไฮเพอร์พารามิเตอร์เพื่อเพิ่มประสิทธิภาพการเรียนรู้ของโมเดล

ค่า Regularisation (C ) คือการปรับขนาดของเรกูลาไรซ์เพื่อการป้องกันการเรียนรู้เกินขอบเขตที่กำหนดด้วยการแบ่งข้อมูลส่วนหนึ่งมาใช้ตรวจสอบ 
ถ้าเรียนรู้มากไป หรือ น้อยเกินไปอาจจะทำให้เกิดความผิดพลาดของการทำนายผลข้อมูลของโมเดลได้

ค่า Gamma คือ อัตราการลดค่าตามระยะห่างจากเส้นแบ่ง Class ใช้ร่วมกับ RGF Kernel และค่า C

ในกรณีที่เขียนโปรแกรมจริงๆเราจะใช้ GridSearchCV มาใช้ปรับเปลี่ยนค่าพารามิเตอร์ (Tuning Parameter) 
ที่เหมาะสมกับโมเดลทำให้โมเดลที่สร้างขึ้นมีประสิทธิภาพที่ดีที่สุด
'''
#train data to model
grid=GridSearchCV(model,param)
grid.fit(x_train,y_train)
#print(grid.best_params_)#ค่าที่ดีที่สุดที่เหมาะสมกับ rbf Kernel
#print(grid.best_estimator_)#ค่าที่ดีที่สุดเหมาะกับ model ที่เราสร้าง

model=grid.best_estimator_
#predict
y_pred=model.predict(x_test)

fig,ax=plt.subplots(4,6)
for i,axi in enumerate(ax.flat):
    axi.imshow(x_test[i].reshape(62,47),cmap='bone')
    axi.set(xticks=[],yticks=[])
    axi.set_ylabel(faces.target_names[y_pred[i]].split()[-1],
    color='green' if y_pred[i] == y_test[i] else 'red')#ทายถูกชื่อสีเขียว ทายผิดชื่อสีแดง
plt.show()

print("Acccuracy = " ,accuracy_score(y_test,y_pred) *100)

mat=confusion_matrix(y_test,y_pred)#ตาราง
sb.heatmap(mat.T, square=True,annot=True,fmt='d',cbar=False,
xticklabels=faces.target_names,
yticklabels=faces.target_names)
plt.xlabel("True Data")
plt.ylabel("Predict Data")
plt.show()
'''
https://seaborn.pydata.org/generated/seaborn.heatmap.html
seaborn.heatmap
squarebool, optional
If True, set the Axes aspect to “equal” so each cell will be square-shaped. 
หากเป็น True ให้ตั้งค่าด้าน Axes เป็น "เท่ากับ" เพื่อให้แต่ละเซลล์มีรูปสี่เหลี่ยมจัตุรัส

annotbool or rectangular dataset, optional
If True, write the data value in each cell. If an array-like with the same shape as data, then use this to 
annotate the heatmap instead of the data. Note that DataFrames will match on position, not index.
ถ้าเป็น True ให้เขียนค่าข้อมูลในแต่ละเซลล์ หากมีลักษณะเหมือนอาร์เรย์ที่มีรูปร่างเหมือนกับdataให้ใช้สิ่งนี้เพื่อใส่คำอธิบายประกอบในแผนที่ความหนาแน่นแทนข้อมูล 
โปรดทราบว่า DataFrames จะจับคู่กับตำแหน่ง ไม่ใช่ดัชนี

cbarbool, optional
Whether to draw a colorbar.
สีของเส้นที่จะแบ่งแต่ละเซลล์
'''