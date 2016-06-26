import pandas
import numpy as np
from sklearn.svm import SVC

raw = pandas.read_csv('svm.csv', header=None)

y = raw.ix[:, 0]
X = raw.ix[:, 1:3]

X = np.array(X)
y = np.array(y)

svm = SVC(C=100000, kernel='linear', random_state=241)
svm.fit(X, y) 

print svm.support_
