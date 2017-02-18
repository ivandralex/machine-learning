from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection
from sklearn import svm
import numpy as np

newsgroups = datasets.fetch_20newsgroups(subset='all', categories=['alt.atheism', 'sci.space'])

y = newsgroups.target

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(newsgroups.data)

feature_mapping = vectorizer.get_feature_names()

grid = {'C': np.power(10.0, np.arange(-5, 6))}
cv = model_selection.KFold(n_splits=5, shuffle=True, random_state=241)
clf = svm.SVC(kernel='linear', random_state=241)
gs = model_selection.GridSearchCV(clf, grid, scoring='accuracy', cv=cv, n_jobs=4)
gs.fit(X, y)

best = gs.cv_results_['params'][gs.best_index_]
print best

clf = svm.SVC(C=best['C'], kernel='linear', random_state=241)
clf.fit(X, y)

coef = clf.coef_.todense().A1

coef_map = []

for i,c in enumerate(coef):
    coef_info = {'index': i, 'coef': abs(c)}
    coef_map.append(coef_info)

newlist = sorted(coef_map, key=lambda k: -k['coef'])

words = []

for info in newlist[0:10]:
    words.append(feature_mapping[info['index']])

print words

words = sorted(words)
print ','.join(words)
