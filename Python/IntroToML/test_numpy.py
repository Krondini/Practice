import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
import pandas as pd

x = np.array([[1,2,3], [4,5,6]])
print('x:\n{}'.format(x), end='\n\n')

#Create Numpy array in Reduced Row Echeleon Form
eye = np.eye(4)
print("Numpy array:\n{}".format(eye), end='\n\n')

#Convert np array to a scipy sparse array in CSR form
#Only non-zero entries are stored
sparse_matrix = sparse.csr_matrix(eye)
print("Sparse array:\n{}".format(sparse_matrix), end='\n\n')

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO representation:\n{}".format(eye_coo), end='\n\n')


x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y, marker='x')
# plt.show()


data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
		'Location': ['New York', 'Paris', 'Berlin', 'London'],
		'Age': [24, 15, 53, 33]
		}

data_pandas = pd.DataFrame(data)
display(data_pandas)