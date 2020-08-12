#Importing the csv file into the python.
import csv

from numpy.core._multiarray_umath import ndarray

with open('winequality-white.csv', 'r') as f:
    wines = list(csv.reader(f, delimiter=';'))

#Importing the numpy module
import numpy as np
wines = np.array(wines[1:],dtype=np.float)

#Checking shape of the array
print(wines.shape)


#Printing the type of the wines
print(type(wines))

#Printing the mean of the wines
W1 = np.mean(wines)
W3 = np.round(W1,2)
print(W3)

#Printing the standard Deviation of the white wines
white = np.std(wines)
print(white)

#Slicing using numpy array
w2 = wines[3,:]
print(w2)

#Iterating using for loop. Going through element one by one
for x in wines:
    print(x)

#Splitting the array
newarr = np.array_split(wines,  2, axis=1)
print(newarr)

#Finding indexes where value is odd
x = np.where(wines%2 ==1)
print(x)

#Finding indexes where value is even
x1 = np.where(wines%2 ==0)
print(x1)

#Generating random number
wines.dtype()
