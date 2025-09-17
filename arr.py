#arr=[1,2,3,4,5]
#arr.append(6)
#print(arr)

#arr.remove(4)
#print(arr)

#arr.insert(3,4)
#print(arr)

#arr.pop()
#print(arr)

#arr.reverse()
#print(arr)

#rr2=[2,3,4,5,6,1]
#arr2.sort()
#print(arr2)

#access element
#arr=[10,20,30,40,50]
#print(arr[1])
#print(arr[:3])
#print(arr[2:])
#print(arr[2:4])

#multidimentional array
import numpy as np
matrix=np.matrix([[1,2,3],[4,5,6]])
#print(matrix[1,1])
#print(matrix[:,0])
#print(matrix[0,:])

matrix=np.zeros((2,2))
#print(matrix)

matrix=np.ones((2,4))
#print(matrix)

matrix=np.eye(4)
#print(matrix)

matrix=np.linspace(1,10,2)
print(matrix)

matrix=np.arange(1,10,3)
print(matrix)