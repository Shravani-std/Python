

# Data Preprocessing Tools

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('/content/drive/MyDrive/Dataset/data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print("Initial X:\n", X)
print("Initial y:\n", y)

from google.colab import drive
drive.mount('/content/drive')

# Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print("X after handling missing data:\n", X)

# Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

if X.size == 0:
    print("Error: X is empty. Please check previous operations.")
else:
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
    X = (ct.fit_transform(X))
    print(X)

    # Encoding the Dependent Variable
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y)
    print(y)

# Encoding the Dependent Variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print("Encoded y:\n", y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print("X_train:\n", X_train)
print("X_test:\n", X_test)
print("y_train:\n", y_train)
print("y_test:\n", y_test)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler(with_mean=False)
# Assuming that after OneHotEncoding, the first few columns are categorical (after encoding),
# we apply scaling only to the numerical columns (columns after the categorical columns).
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
print("Training set after feature scaling (X_train):")
print(X_train)
print("Test set after feature scaling (X_test):")
print(X_test)