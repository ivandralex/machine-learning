import pandas
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

raw = pandas.read_csv('perceptron-train.csv', header=None)
raw_test = pandas.read_csv('perceptron-test.csv', header=None)

X = np.array(raw.ix[:, 1:3])
y = np.array(raw.ix[:, 0])
X_test = np.array(raw_test.ix[:, 1:3])
y_test = np.array(raw_test.ix[:, 0])

clf = Perceptron(random_state=241)
clf.fit(X, y)
y_predictions = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_predictions)
print accuracy

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = np.array(raw.ix[:, 1:3])
y_train = np.array(raw.ix[:, 0])
X_test = np.array(raw_test.ix[:, 1:3])
y_test = np.array(raw_test.ix[:, 0])

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = Perceptron(random_state=241)
clf.fit(X_train_scaled, y)
y_predictions = clf.predict(X_test_scaled)

accuracy_scaled = accuracy_score(y_test, y_predictions)
print accuracy_scaled

print accuracy_scaled - accuracy