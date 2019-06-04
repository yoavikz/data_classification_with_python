#This is the classification script
#Importing relevant libraries
from sklearn import linear_model
from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

#Runnint all ~1400 train rows as train and ~700 test rows as test to predict labels

#opening the Train file to 2D numpy array
#the lables will be in y variable as 1D array in matching order to X
#test is an array of unlabeled rows of data to be labeled in this code

out=open("classification.csv",'w')
train_data = np.genfromtxt('TrainDataset.csv', skip_header=True,delimiter=',')
test_data=np.genfromtxt('TestDataset.csv', skip_header=True,delimiter=',')

X = train_data[:, 1:]
y = train_data[:, 0]
test= test_data[:, 1:]

X=np.nan_to_num(X)
y=np.nan_to_num(y)
test=np.nan_to_num(test)

X=np.round(X,5)
y=np.round(y,5)
test=np.round(test,5)
model = GaussianNB() 
#Predict Output
model.fit(X,y)
predicted= model.predict(test)
out.write("row ID,Predicted Label\n")

for i,j in zip(test_data,predicted):
    out.write("{},{}\n".format(str(i[0]),str(j)))
out.close()
print(model.score(X,y))
