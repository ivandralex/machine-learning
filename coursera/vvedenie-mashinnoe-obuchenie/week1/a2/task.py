import pandas
import numpy as np
from sklearn.tree import DecisionTreeClassifier

raw = pandas.read_csv('../titanic.csv', index_col='PassengerId')
data = pandas.DataFrame()
data['Sex'] = raw['Sex']
data['Sex'][data['Sex'] == 'male'] = 1
data['Sex'][data['Sex'] == 'female'] = 0 
data['Age'] = raw['Age'][raw['Age'].notnull()]
data['Pclass'] = raw['Pclass']
data['Fare'] = raw['Fare']
data = data[data['Age'].notnull()]

X = np.array(data)
y = raw['Survived'][raw['Age'].notnull()]
y = np.array(y)
print X[0:10]
print y[0:10]

clf = DecisionTreeClassifier()
clf.fit(X, y)

importances = clf.feature_importances_
print(importances)

print data[0:1]