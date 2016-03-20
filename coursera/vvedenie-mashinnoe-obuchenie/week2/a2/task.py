import pandas
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.cross_validation import cross_val_score
from  sklearn.datasets import load_boston
from sklearn.cross_validation import KFold
from sklearn.preprocessing import scale

raw = load_boston()
raw.data = scale(raw.data)

print raw.data.shape
print raw.target.shape
#print len(raw.target)

accuracies = []
ps = []

steps = np.linspace(1, 10, 200)

for p in steps:
	kf = KFold(len(raw.target), n_folds=5, shuffle=True, random_state=42)
	rg = KNeighborsRegressor(n_neighbors=5, weights='distance', p=p, metric='minkowski')
	metrics = cross_val_score(rg, raw.data, raw.target, cv=kf, scoring='mean_squared_error')
	print metrics
	accuracies.append(np.mean(metrics))
	ps.append(p)

print len(accuracies)
print accuracies
print ps[np.argmax(accuracies)], np.max(accuracies)

#sklearn.cross_validation.cross_val_score
#sklearn.preprocessing.scale