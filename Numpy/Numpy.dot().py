import numpy as np
product = np.dot(4,5)
print("The Product of the Scalar value is " ,product)

vector_1 = 2+3j
vector_2 = 4+5j
print("The Vector 1 is ",vector_1)
print("The Vectoe 2 is ",vector_2)
product1 = np.dot(vector_1,vector_2)
print("The dot Product of the Two vector is ")
print(product1)

vec1 = np.array([[1,4],[5,6]])
vec2 = np.array([[2,4],[5,2]])
print("The Dot Product of the two Vector is ")
print(np.dot(vec1,vec2))
