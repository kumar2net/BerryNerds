# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 08:58:03 2017

@author: kua
"""
def lbl(vtype):
    if vtype == 'sportscar':
        tst3 = 0
    else:    
        tst3 = 1
    return tst3
    
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
data = pd.read_excel('d:/AK_Code/py/AK_clf_data2.xlsx')
data['tst3'] = list(map(lbl, data['Label']))
print(data)
#data.drop(columns=['tst','tst1'],inplace=True)
data.as_matrix(columns=['Horsepower','Seats','tst3'])
features = data.as_matrix(columns=['Horsepower','Seats'])
labels = data.as_matrix(columns=['tst3'])
plt.plot(data['Horsepower'],data['Seats'], 'r*')
plt.xlabel('hp')
plt.ylabel('seat')
plt.title('ML Classifier Lesson')
plt.show
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
clf.predict([[125, 7]])
print(clf.predict([[125, 7]]))
print(clf.predict([[525, 2]]))
