from sklearn import tree
from sklearn.datasets import load_iris

from sklearn.externals.six import StringIO  
import pydot

from IPython.display import Image  

def predictByDTC(X,Y,test):
    clf = tree.DecisionTreeClassifier().fit(X, Y)

    #Visualize decision tree
    #dot_data = StringIO()
    #tree.export_graphviz(clf, out_file=dot_data) 
    #graph = pydot.graph_from_dot_data(dot_data.getvalue())
    #graph.write_pdf("dt.pdf") 

    return clf.predict(test)
    

if __name__ == '__main__':

    iris = load_iris()
    print predictByDTC(iris.data, iris.target, iris.data[0:,])

