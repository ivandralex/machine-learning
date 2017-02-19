from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from scipy.sparse import hstack
from sklearn.linear_model import Ridge
import pandas
import sys
import re

data_train = pandas.read_csv('./salary-train.csv')
data_test = pandas.read_csv('./salary-test-mini.csv')

data_train['FullDescription'] = data_train['FullDescription'].apply(lambda text: text.lower())
data_train['FullDescription'] = data_train['FullDescription'].replace('[^a-zA-Z0-9]', ' ', regex=True)

data_test['FullDescription'] = data_test['FullDescription'].apply(lambda text: text.lower())
data_test['FullDescription'] = data_test['FullDescription'].replace('[^a-zA-Z0-9]', ' ', regex=True)

#Fill missing values
data_train['LocationNormalized'].fillna('nan', inplace=True)
data_train['ContractTime'].fillna('nan', inplace=True)

#Apply one-hot encoding
enc = DictVectorizer()
X_train_categ = enc.fit_transform(data_train[['LocationNormalized', 'ContractTime']].to_dict('records'))
X_test_categ = enc.transform(data_test[['LocationNormalized', 'ContractTime']].to_dict('records'))

vectorizer = TfidfVectorizer(min_df=5)
description_train = vectorizer.fit_transform(data_train['FullDescription'])
description_test = vectorizer.transform(data_test['FullDescription'])


X_train = hstack([description_train, X_train_categ]).toarray()
y_train = data_train['SalaryNormalized'].as_matrix()

X_test = hstack([description_test, X_test_categ]).toarray()

reg = Ridge (alpha=1, random_state=241, copy_X=False)
reg.fit(X_train, y_train)

predicted = reg.predict(X_test)

res = '%.2f %.2f' % (predicted[0], predicted[1])
out = open('./res.txt', 'w+')
out.write(res)
out.close()
