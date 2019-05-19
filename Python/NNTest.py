import sys
import scipy
import numpy
import matplotlib
import matplotlib.pyplot as plt
import pandas
import sklearn


#Ensure that all libraries are installed properly
print("Python: {}".format(sys.version))
print("scipy: {}".format(scipy.__version__))
print("numpy: {}".format(numpy.__version__))
print("matplotlib: {}".format(matplotlib.__version__))
print("pandas: {}".format(pandas.__version__))
print("sklearn: {}\n".format(sklearn.__version__))


#Load in dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
list_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=list_names)


#Dimension of dataset
print(dataset.shape)
print('')


#View first 20 rows of the set
print(dataset.head(20))
print('')


#Descriptions of the dataset
print(dataset.describe())


#Create a histogram
dataset.hist()
plt.show()


array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
