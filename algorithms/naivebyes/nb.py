import numpy as np
from sklearn.naive_bayes import GaussianNB as gnb
from sklearn.naive_bayes import MultinomialNB as mnb
from sklearn.naive_bayes import BernoulliNB as bnb


def predictByGNB(features, classes, test):
    #No parameters need
    clf = gnb()
    clf.fit(features, classes)
    return clf.predict(test)

#Discrete Model
def predictByMNB(features, classes, test):

    ## Why MNB requires non-negative features?
    ## MNB uses multinomial distribution to compute P(x_i|Y_j), which is the distribution of the i_th feature when given class Y_j.
    ## Because multinomial distribution's every value should be >= 0, so MNB ask for it too.
    if (features.min() < 0) :
        raise ValueError("Feautres must be larger than or equal to 0 if using multinomial naive bayes!")
    
    clf = mnb()
    clf.fit(features, classes)
    return clf.predict(test)

#Discrete Model, bettor to give binarize paramter so that it can binarize the features
def predictByBNB(features, classes, test):
    clf = bnb(binarize=2)
    clf.fit(features, classes)
    return clf.predict(test)

if __name__ == '__main__':

    X = np.array([[41, 1], [12, 9], [3, 20], [1, 1], [2, 1], [3, 2]])
    Y = np.array([1, 3, 1, 2, 2, 2])
    test = np.array([[9, 2]])

    print 'BNB: %s' % predictByBNB(X, Y, test)
    print 'GNB: %s' % predictByGNB(X, Y, test)
    print 'MNB: %s' % predictByMNB(X, Y, test)
        
