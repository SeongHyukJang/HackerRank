import numpy as np
np.set_printoptions(sign = ' ')
arr = np.array(list(map(float,input().split())))

print(np.floor(arr), np.ceil(arr), np.rint(arr), sep = '\n')