import numpy as np
x=np.random.randint(1,20,15)
print(x)
y=x.reshape(3,5)
print(y)
new_a = np.where(y == [
    [i]
    for i in np.amax(y, axis = 1)
], 0, y)

print(new_a)