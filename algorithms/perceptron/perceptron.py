# coding=utf-8

import numpy as np
from sklearn import linear_model

#SGDClassfier can be used here too, in the official document, it says:
#Perceptron and SGDClassifier share the same underlying implementation.
#In fact, Perceptron() is equivalent to SGDClassifier(loss=”perceptron”, eta0=1, learning_rate=”constant”, penalty=None).

#A simple data
def calModel(features, classes) :

    clf = linear_model.Perceptron()
    clf.fit(features, classes)


    warn = ''.join(map(lambda x, y : str('' if clf.predict([x]) == y else x), features, classes))
    if warn:
        print 'WARN: the given features is NOT linear seperable!'
    
    return '''
        The model function is:
            sign( %(coef)s + %(intercept)s)
        In it: the sign function is:
            sign(x) = %(class)d, if x < 0
                    = other class, otherwise
    ''' % ({
        'class': classes[0],
        'coef': ' + '.join(map(lambda x, y : '%d*feature_%d' % (x, y), clf.coef_[0], range(len(features[0])))),
        'intercept': clf.intercept_[0]
    })



if __name__ == '__main__':
    #features = np.array([[0, 0], [0, 1], [0, 2], [-1, 0], [-2, -2], [10, 0], [9, 2], [-3, -3], [-1, 3], [-2, 2], [-4, 2], [-5, 9]])
    #classes = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

    features = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1], [0, 0]])
    classes = np.array([1, 1, 2, 2, 1])
    
    print calModel(features, classes)
