#importing the libraries

import numpy as np
import pandas as pd
#import matplotlib as plt
from matplotlib import pyplot as plt
#reading the dataset

dataset = pd.read_csv('Salary_Data.csv')

#putting indepandent variabls value

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values

#taking care of missing datasets

#from sklearn.impute import SimpleImputer

#imputer = SimpleImputer(missing_values=np.nan, strategy= 'mean')

#imputer.fit(X[:, 1:3])

##print(X)

#Encoding cetagoricl data

#from sklearn.preprocessing import OneHotEncoder
#from sklearn.compose import ColumnTransformer
#from sklearn.preprocessing import LabelEncoder#, OneHotEncoder
#labelencoder_X = LabelEncoder()
#X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

#from sklearn.compose import ColumnTransformer
#from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#labelencoder_X = LabelEncoder()
#X[:, 0]=labelencoder_X.fit_transform(X[:, 0])
#ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
#X = np.array(ct.fit_transform(X))
#print(X)
#labelencoder_Y = LabelEncoder()
#Y=labelencoder_Y.fit_transform(Y)
#print(Y)

#Spliting the data in testig and training

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

#feature scalling

#from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)

#Applyring Simple linear regression 

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train, Y_train)

#Predicting the test set result
Y_pred = regressor.predict(X_test)

#visualizing the training set result

plt.scatter(X_train, Y_train, color='red')

plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title ('Salary vs Eexperience(Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#visualizing the testing set result

plt.scatter(X_test, Y_test, color='red')

plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title ('Salary vs Eexperience(Testing set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()