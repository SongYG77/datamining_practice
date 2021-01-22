import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.datasets import load_digits

digits = load_digits()
X = digits.data
y = digits.target
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y,test_size=0.3,train_size=0.7,random_state=1)
model = tree.DecisionTreeClassifier()
model = model.fit(Xtrain,ytrain)
y_pred = model.predict(Xtest)
a = accuracy_score(ytest, y_pred)
print(a)