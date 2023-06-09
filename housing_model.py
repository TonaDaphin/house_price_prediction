# -*- coding: utf-8 -*-
"""DataMunging.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DN8YaMbgfbUcx26lfqLYxDk_odMdxGwa
"""

"""## Housing

"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

df=pd.read_csv('/content/drive/My Drive/Colab Notebooks/AI/Colab Notebooks/housing.csv')



df.head()

df.info()

df['ocean_proximity'].value_counts()

df.describe()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
# only in a Jupyter notebook
import matplotlib.pyplot as plt
housing=df
housing.hist(bins=50, figsize=(20,15))
plt.show()

housing.plot(kind="scatter", x="longitude", y="latitude")

housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)

housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4, s=housing["population"]/100, label="population", c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True, )
plt.legend()

corr_matrix = housing.corr()

corr_matrix

corr_matrix["median_house_value"].sort_values(ascending=False)

housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_house"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"]=housing["population"]/housing["households"]
corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)

housing.info()

import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

numeric=housing.select_dtypes(include=np.number)
imp = IterativeImputer(max_iter=1, random_state=0)
imp.fit(numeric)
imputed_numeric=np.round(imp.transform(numeric))

imputed_numeric.shape

numeric.columns

num_data=pd.DataFrame(imputed_numeric,columns=numeric.columns)

num_data.info()

num_data.head(5)

housing.head(5)

ocean=pd.get_dummies(housing['ocean_proximity'], prefix='ocean_')

ocean.head(5)

ocean.tail(5)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
scaled=sc.fit_transform(num_data)
scaled

num=pd.DataFrame(scaled,columns=num_data.columns)

df=pd.concat([num,ocean], axis=1)

df.head(5)

df.shape

from sklearn.model_selection import train_test_split

y=df['median_house_value']
X=df.drop('median_house_value',axis=1)

Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,y,test_size=0.2,random_state=42)

Xtrain.shape

Xtest.shape

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()

lin_reg.fit(Xtrain, Ytrain)

y_pred=lin_reg.predict(Xtest)

from sklearn.metrics import mean_absolute_error

mean_absolute_error(y_pred,Ytest)

