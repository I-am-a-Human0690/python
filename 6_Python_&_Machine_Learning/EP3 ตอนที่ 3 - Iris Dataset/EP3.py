
from sklearn  import datasets
iris_datasct=datasets.load_iris()
print('keys')
print(iris_datasct.keys())
print('target')
print(iris_datasct['target'])
print(iris_datasct.target)#แบบนี้ก็ได้
print('target_names')
print(iris_datasct['target_names'])
print('DESCR')
print(iris_datasct['DESCR'])
print('feature_names')
print(iris_datasct['feature_names'])
print('data')
print(iris_datasct['data'])
print('data[0:10]')
print(iris_datasct['data'][0:10])
'''
https://notebooks.githubusercontent.com/view/ipynb?color_mode=auto&commit=fe99c1efbf290344f667903946c08df96d3ec51e&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f676973742f612d6b7269726b2f37646664626161383635396364656664303165383433363265613235383661622f7261772f666539396331656662663239303334346636363739303339343663303864663936643365633531652f7363696b69742d6c6561726e2d696e74726f2e6970796e62&logged_in=false&nwo=a-krirk%2F7dfdbaa8659cdefd01e84362ea2586ab&path=scikit-learn-intro.ipynb&repository_id=112954884&repository_type=Gist

Scikit-learn Intro
สำหรับเนื้อหาที่เกี่ยวข้องกับ scikit-learn ในบทนี้จะเขียนให้เห็นภาพรวมของ scikit-learn ทั้งหมดว่า scikit-learn คืออะไร ประกอบด้วยอะไรบ้าง และตัวอย่างการนำไปใช้งาน

Scikit-learn คืออะไร ??
Scikit-learn เป็น library ของภาษา Python ที่นิยมใช้กันมากที่สุดในการทำ machine learning เพราะสามารถทำงานได้อย่างมีประสิทธิภาพ และมี algorithm ให้เลือกใช้ได้อย่างหลากหลาย นอกจากนี้ scikit-learn ยังสามารถนำมาใช้งานร่วมกับ library Numpy และ Pandas ได้ มีเอกสารการใช้งานพร้อมตัวอย่างประกอบให้ดูแบบครบถ้วนทำให้ง่ายต่อการนำมาใช้งาน

Scikit-learn ประกอบไปด้วยอะไรบ้าง ??
Scikit-learn จะแบ่งออกเป็น 10 หมวดหมู่ตามประเภทการใช้งาน ได้แก่

Supervised learning เช่น
Linear Model
Support Vector Machines
Kernel ridge regression
Decision Trees
ฯลฯ
Unsupervised learning เช่น
Manifold learning
Clustering
Biclustering
Density Estimation
ฯลฯ
การเลือกโมเดลและการประเมินผล เช่น
Cross-validation
Tuning the hyper-parameters of an estimator
Metrics and scoring
Validation curves
การตรวจสอบ เช่น
Partial Dependence and Individual Conditional Expectation plots
Permutation feature importance
การสร้างกราฟ เช่น
ส่วนเสริมที่มีอยู่ในการสร้างกราฟ
การแปลงชุดข้อมูล เช่น
Pipelines and composite estimators
Feature extraction
Preprocessing data
Imputation of missing values
ฯลฯ
ชุดข้อมูลส่วนเสริม เช่น
ชุดข้อมูลสำหรับทดลองใช้งาน
ชุดข้อมูลจริง
ชุดข้อมูลที่ถูกสร้างขึ้น
การโหลดชุดข้อมูลอื่น
การคำนวณด้วย scikit-learn เช่น
กลยุทธ์การคำนวณเพื่อปรับขนาดข้อมูล
ประสิทธิภาพการคำนวณ
ความขนาน, การจัดการแหล่งข้อมูล, การกำหนดค่า
Model persistence
Python specific serialization
Interoperable formats
ข้อผิดพลาดที่พบเห็นบ่อยและการแนะนำแนวทางปฏิบัติ
การเตรียมข้อมูลที่ไม่สอดคล้องกัน
การรั่วไหลของข้อมูล
การควบคุมการสุ่ม
'''