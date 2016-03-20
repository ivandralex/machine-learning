import pandas
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn.preprocessing import scale

raw = pandas.read_csv('wine.data', header=None)


print raw.keys()

y = raw.ix[:, 0]
X = raw.ix[:, 1:14]
X = scale(X)

print raw.shape
print X.shape
print y.shape

X = np.array(X)
y = np.array(y)

kf = KFold(len(y), n_folds=5, shuffle=True, random_state=42)

accuracies = [0]

for k in range(1, 51):
	clf = KNeighborsClassifier(n_neighbors=k)
	metrics = cross_val_score(clf, X, y, cv=kf, scoring='accuracy')
	accuracies.append(np.mean(metrics))




print accuracies
print np.argmax(accuracies), np.max(accuracies)

#sklearn.cross_validation.cross_val_score
#sklearn.preprocessing.scale