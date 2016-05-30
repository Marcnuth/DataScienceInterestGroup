'''
In this file, we will use KNN to classify data

How to use the scikit of KNN, please refer to:
http://scikit-learn.org/stable/modules/neighbors.html
'''

from sklearn import neighbors, datasets


def calModel(k, features, classes) :
    # the weights can be uniform or distance
    # For uniform: for the k neighbors, their weight are the same
    # For distance: for k neigbors, the nearer one has big weight

    # The algorithm here can be auto, kd_tree, ball_tree, brute
    # For auto, it will select algorithm autoly.
    # For brute, it will compare every point to calculate neighbors brutely. This is not recommended.
    # For kd_tree, it will use kd_tree to select neighbors. This is better time-saving than brute algorithm.
    # For ball_tree, it use ball_tree algorithm. For features dimension > 20, this method is suggested, cause kd_tree will encounter dimension disaster.
    clf = neighbors.KNeighborsClassifier(k, weights='uniform', algorithm='kd_tree')
    clf.fit(features, classes)

    print 'The accuracy(Correctly classified / All data) = %f' % clf.score(features, classes)



if __name__ == "__main__":

    # Only use two features here
    data = datasets.load_iris()
    features = data.data[:, :2]
    classes = data.target

    calModel(10, features, classes)
