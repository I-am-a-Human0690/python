'''
สรุป Machine Learning(EP.5)-การจัดหมวดหมู่ด้วย Naive Bayes
https://kongruksiam.medium.com/%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B-machine-learning-ep-5-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%AB%E0%B8%A1%E0%B8%A7%E0%B8%94%E0%B8%AB%E0%B8%A1%E0%B8%B9%E0%B9%88%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-naive-bayes-eb9ce0e1b010
'''
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
#load dataset
iris=load_iris()

#assign attribute , target
x=iris['data']
y=iris['target']
# print(x)
# print(y)

# train , test
x_train,x_test,y_train,y_test=train_test_split(x,y)

#model
model=GaussianNB()

#train
model.fit(x_train,y_train)

#prediction
y_pred=model.predict(x_test)

#Accuracy Score
print("Accuracy = ",accuracy_score(y_test,y_pred))