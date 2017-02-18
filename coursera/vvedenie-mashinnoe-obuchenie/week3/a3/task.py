from sklearn.metrics import roc_auc_score
import numpy as np
import pandas
import math

data = pandas.read_csv('./data-logistic.csv', header=None).as_matrix()

def sigmoid(row, w):
    return 1 / (1 + math.exp(-w[0]*row[1] - w[1]*row[2]))


def gradient_descent(data, C):
    k = 0.1
    eps = 1e-5
    n = 10000
    l = len(data)

    w = [0, 0]
    newW = [0, 0]

    #Run gradient descent
    for step in range(n):
        for j in range(2):
            s = 0
            for row in data:
                s = s + row[0]*row[j+1]*(1 - 1 / (1 + math.exp(-row[0]*(w[0]*row[1] + w[1]*row[2]))))
            newW[j] = w[j] + k/l*s - k*C*w[j]

        #Check if calculations converged
        stop = False
        if math.hypot(newW[0]-w[0], newW[1]-w[1]) < eps:
            stop = True
        #Update weights simultaneously
        w[0] = newW[0]
        w[1] = newW[1]
        if stop:
            print 'Gonna stop'
            break


    return w

y_ground = map(lambda row: row[0], data)

w = gradient_descent(data, 0)
print "Weights: %s" % w
y_predicted = map(lambda row: sigmoid(row, w), data)
score = roc_auc_score(y_ground, y_predicted)
print "Score: %.4f" % score

w = gradient_descent(data, 10)
print "Weights with reg: %s" % w
y_predicted = map(lambda row: sigmoid(row, w), data)
score_reg = roc_auc_score(y_ground, y_predicted)
print "Score with reg: %.4f" % score_reg

res = "%.3f %.3f" % (score, score_reg)

out = open('./res.txt', 'w+')
out.write(res)
out.close()
