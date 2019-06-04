#This is the validation script
#Importing relevant libraries
from sklearn import linear_model
from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

#Runnint 1000 rows as train and 400 rows as "test" to check algorithm accuracy
#VS an already known set of data

#opening the Train1000 file to 2D list, without lables - then put in X variable
#as a 2D numpy array 
#the lables will be in train_y variable as 1D list in matching order to X
#test variable which hold the test dataset is actually the 400 rows from original
#Train file which is used here to validate algorithm accuracy

out=open("validation.csv",'w')
train_data = np.genfromtxt('Train_1000.csv', skip_header=True,delimiter=',')
test_data=np.genfromtxt('TrainValidation400.csv', skip_header=True,delimiter=',')

X = train_data[:, 1:]
y = train_data[:, 0]
val= test_data[:, 1:]

X=np.nan_to_num(X)
y=np.nan_to_num(y)
test=np.nan_to_num(test)

# X=X.astype(float)
# y=y.astype(float)
# test=test.astype(float)

X=np.round(X,5)
y=np.round(y,5)
test=np.round(test,5)

if np.isnan(X.any())==False:
    model = GaussianNB() 
    #Predict Output
    model.fit(X,y)
    predicted= model.predict(test)
    out.write("Known,Predicted\n")
    for i,j in zip(test_data,predicted):
        out.write("{},{}\n".format(str(i[0]),str(j)))
out.close()
print(model.score(X,y))