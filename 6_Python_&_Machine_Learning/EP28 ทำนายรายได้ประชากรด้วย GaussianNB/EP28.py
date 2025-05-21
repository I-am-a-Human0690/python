'''
คาดการณ์ว่ารายได้จะเกิน $50K/ปี โดยอิงจากข้อมูลสำมะโนประชากร
https://www.kaggle.com/datasets/uciml/adult-census-income
'''
'''
sklearn.preprocessing.LabelEncoder
https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
'''
import pandas as pd
from sklearn.preprocessing import LabelEncoder#เข้ารหัสหมวดหมู่
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

dataset=pd.read_csv("C:\\Users\\WTFTHE\\Desktop\\code\\Python\\6Python & Machine Learning\\adult.csv")
print(dataset.head())

def cleandata(dataset):#จัดกลุ่มให้กลายเป็นตัวเลข
    for column in dataset.columns:
        if dataset[column].dtype == type(object):
            le = LabelEncoder()
            dataset[column]=le.fit_transform(dataset[column])
    return dataset

def split_feature_class(dataset,feature):
    features=dataset.drop(feature,axis=1)  # เอาข้อมูลทั้งหมดยกเว้น income
    labels=dataset[feature].copy() #เอาเฉพาะข้อมูล income
    return features,labels

dataset=cleandata(dataset)
print(dataset.head())

#split train ,test
training_set,test_set=train_test_split(dataset,test_size=0.2)

#train
train_features,train_labels=split_feature_class(training_set,"income")

#test
test_features,test_labels=split_feature_class(test_set,"income")

print("="*150)
print('train_features')
print(train_features)
print('train_labels')
print(train_labels)

#model
model=GaussianNB()
model.fit(train_features,train_labels)

#predict
clf_pred=model.predict(test_features)

print("Accuracy = ",accuracy_score(test_labels,clf_pred))