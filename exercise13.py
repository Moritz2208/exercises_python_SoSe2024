import numpy as np
from math import log10

x = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]

x_log = [log10(k) for k in x]

x_array_log = np.log10(x)
