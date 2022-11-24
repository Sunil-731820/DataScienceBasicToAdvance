import numpy as np
# When axis is equal to None
print("Bool value with axis = NONE:",np.all(
    [[True,False],[True,True]]
))

# When axis is equal to 0

print("Bool Value with axis is 0 ",np.all(
    [[True,False],[True,True]], axis=0
))

print(np.all([0,np.nan]))