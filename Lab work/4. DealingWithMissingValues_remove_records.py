

from pandas import read_csv
import numpy
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
dataset = read_csv('pima-indians-diabetes.csv',header=None)
dataset.shape
# mark zero values as missing or NaN
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, numpy.NaN)
# drop rows with missing values
dataset.dropna(inplace=True)
dataset.shape
# split dataset into inputs and outputs
values = dataset.values
X = values[:,0:8]
y = values[:,8]
model = LinearDiscriminantAnalysis()
kfold = KFold(n_splits=3, random_state=7)
result = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
print(" Accuracy of Model :")
print(result.mean())