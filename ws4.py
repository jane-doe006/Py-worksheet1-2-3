# Question 1: Array Creation  
# 1.1 Create a 1D array of integers from 5 to 25 using NumPy. 
# 1.2 Create a 2D array with 3 rows and 4 columns filled with random integers between 10 and 50. 

import numpy as np
array=np.arange(5,26)
print(array)
array1=np.random.randint(10,50,size=(3,4))
print(array1)
# Question 2: Array Attributes  
# 2.1 For the 1D array created in Question 1.1, find, and print its: 
#  Shape 
#  Size 
#  Data type 
# 2.2 For the 2D array created in Question 1.2, find, and print its: 
#  Shape 
#  Size 
#  Data type 

import numpy as np
array=np.arange(5,26)
print(array)
print(np.shape(array), np.size(array), type(array))
array1=np.random.randint(10,50,size=(3,4))
print(array1)
print(np.size(array1),np.shape(array1),type(array1))

# Question 3: Array Operations  
# 3.1 Create two 1D arrays: 
#  Array1: [2, 4, 6, 8, 10] 
#  Array2: [1, 3, 5, 7, 9] 
# 3.2 Perform the following operations and print the results: 
#  Addition 
#  Subtraction 
#  Element-wise multiplication 
#  Element-wise division 

import numpy as np 
array1=np.array([2,4,6,8,10])
array2=np.array([1,3,5,7,9])
print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)

# Question 4: Broadcasting  
# 4.1 Create a 2D array of shape (3, 3) with values starting from 1 to 9. 
# 4.2 Using broadcasting, multiply this 2D array by a scalar value of 5. Print the result. 

import numpy as np 
a=np.arange(1,10).reshape(3,3)
print(a*5)

# Question 5: Slicing and Indexing  
# 5.1 Create a 2D array of shape (4, 4) with values ranging from 10 to 25. 
# 5.2 Extract the second row and the last column of the array. 
# 5.3 Replace the elements of the first row with zeros. 

import numpy as np 
a=np.random.randint(10,25,size=(4,4))
print(a)
print(a[1,:],a[:,-1])
b=np.zeros(a[0])
print(b)

# Question 6: Boolean Indexing  
# 6.1 Create a 1D array with random integers between 20 and 40 (10 elements). 
# 6.2 Use Boolean indexing to find all elements greater than 30.

import numpy as np 
a=np.random.randint(20,41,size=10)
for i in range(len(a)):
    if a[i]>30:
        print(True)

# Question 7: Reshaping  
# 7.1 Create a 1D array with 12 elements starting from 11. 
# 7.2 Reshape it into a 2D array of shape (3, 4). Print the reshaped array.

import numpy as np 
a=np.arange(11,23)
print(a)
b=a.reshape(3,4)
print(b)

# Question 8: Matrix Operations  
# 8.1 Create two 2x2 matrices: 
#  Matrix A: [[1, 2], [3, 4]] 
#  Matrix B: [[5, 6], [7, 8]] 
# 8.2 Perform and print the results of the following operations: 
#  Matrix multiplication 
#  Transpose of Matrix A 

import numpy as np 
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a*b, np.transpose(a))

# Question 9: Statistical Functions  
# 9.1 Create a 1D array with random integers between 10 and 60 (15 elements). 
# 9.2 Compute and print the following statistics: 
#  Mean 
#  Median 
#  Standard deviation 

import numpy as np 
a=np.random.randint(10,61,size=15)
print(a)
print(np.mean(a),np.median(a),np.std(a))

# Question 10: Linear Algebra  
# 10.1 Create a 3x3 matrix: 
#  [
#  2 1 3
#  0 5 6
#  7 8 9
#  ] 
# 10.2 Perform the following operations: 
#  Find the determinant of matrix A. 
#  Compute the inverse of matrix A. 
#  Find the eigenvalues and eigenvectors of matrix A.

import numpy as np 
a=np.array([[2,1,3],[0,5,6],[7,8,9]])
print(a)
print(np.linalg.det(a),np.linalg.inv(a),np.linalg.eigvals(a))

# Question 11: A mobile robot moves in a 2D environment, and its positions (x, y) are recorded at 
# different time steps. The dataset of robot positions is stored in a NumPy array. Data  (x,y)  (0,0), 
# (2,3), (4,7), (7,10), (10,15). 
# 11.1 Which NumPy command will correctly compute the Euclidean distance traveled between the first 
# and last recorded positions of the robot? 
# 11.2 To compute the total distance traveled by the robot (step by step), which NumPy command is 
# most appropriate?

#np.linalg.norm() calculates disctances by euclidian formula