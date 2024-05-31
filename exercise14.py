import numpy as np

y = [2, 3, 8, 4, 10, 1, 9, 5, 1, 0]

print (np.sqrt(1/len(y) * sum((y - np.mean(y))**2)))

print(np.std(y))
