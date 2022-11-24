import numpy as np
array = [
    [5,6,2,7,1],
    [4,9,2,9,3]
]
print("The Array is ")
print(array)

print("taking Indeces is ")
print(np.take(array,[0,4]))
print("Again the use of the take()")
print(np.take(array,[[0,1],[2,3]]))

