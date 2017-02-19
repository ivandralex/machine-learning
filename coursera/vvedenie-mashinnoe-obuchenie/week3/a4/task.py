import sklearn.metrics as metrics
import numpy as np
import pandas
import math

#1
data = pandas.read_csv('./classification.csv')

tp = len(data[(data['true'] == data['pred']) & (data['true'] == 1)])
fp = len(data[(data['true'] != data['pred']) & (data['pred'] == 1)])
fn = len(data[(data['true'] != data['pred']) & (data['pred'] == 0)])
tn = len(data[(data['true'] == data['pred']) & (data['true'] == 0)])

res = "%s %s %s %s" % (tp, fp, fn, tn)
out = open('./res1.txt', 'w+')
out.write(res)
out.close()

#2
accuracy = metrics.accuracy_score(data['true'], data['pred'])
precision = metrics.precision_score(data['true'], data['pred'])
recall = metrics.recall_score(data['true'], data['pred'])
f = metrics.f1_score(data['true'], data['pred'])

a2 = 1.0 * (tp + tn) / (tp + fp + fn + tn)
p2 = 1.0 * tp / (tp + fp)
r2 = 1.0 * tp / (tp + fn)
f2 = 2 * p2 * r2 / (p2 + r2)

#print "accuracy: %s vs %s" % (accuracy, a2)
#print "precision: %s vs %s" % (precision, p2)
#print "recall: %s vs %s" % (recall, r2)
#print "f score: %s vs %s" % (f, f2)

res = "%.2f %.2f %.2f %.2f" % (accuracy, precision, recall, f)
out = open('./res2.txt', 'w+')
out.write(res)
out.close()

#3
data = pandas.read_csv('./scores.csv')

models = ['score_logreg','score_svm','score_knn','score_tree']

roc_auc_score = 0;
best_model = ''

for model in models:
    score = metrics.roc_auc_score(data['true'], data[model])
    if score > roc_auc_score:
        roc_auc_score = score
        best_model = model

res = "%s" % (best_model)
out = open('./res3.txt', 'w+')
out.write(res)
out.close()

#4
precision = 0;
best_model = ''

for model in models:
    precisions, recall, thresholds = metrics.precision_recall_curve(data['true'], data[model])
    p = 0
    for i,r in enumerate(recall):
        if r > 0.7 and precisions.item(i) > p:
            p = precisions.item(i)
    if p > precision:
        precision = p
        best_model = model

res = "%s" % (best_model)
out = open('./res4.txt', 'w+')
out.write(res)
out.close()
