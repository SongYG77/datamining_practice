from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import keras
iris = load_iris()
fnames = list(iris.feature_names)
print(fnames)
data = {iris.feature_names[0] : iris.data[:,0],
        iris.feature_names[1]: iris.data[:, 1],
        iris.feature_names[2]: iris.data[:, 2],
        iris.feature_names[3]: iris.data[:, 3],
        }
frame = pd.DataFrame(data)
frame['target'] = iris.target
frame['targetName'] = iris.target_names[frame['target']]
d0 = frame[frame['target']==0]
d1 = frame[frame['target']==1]
d2 = frame[frame['target']==2]
plt.figure()
plt.plot(d0['sepal length (cm)'], d0['sepal width (cm)'], 'or', label = iris.target_names[0])
plt.plot(d1['sepal length (cm)'], d1['sepal width (cm)'], 'xb', label = iris.target_names[1])
plt.plot(d2['sepal length (cm)'], d2['sepal width (cm)'], '^g', label = iris.target_names[2])
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.legend()
plt.figure()
plt.plot(d0['petal length (cm)'], d0['petal width (cm)'], 'or', label = iris.target_names[0])
plt.plot(d1['petal length (cm)'], d1['petal width (cm)'], 'xb', label = iris.target_names[1])
plt.plot(d2['petal length (cm)'], d2['petal width (cm)'], '^g', label = iris.target_names[2])
plt.xlabel('petal length (cm)')
plt.ylabel('sepal width (cm)')
plt.legend()
plt.show()