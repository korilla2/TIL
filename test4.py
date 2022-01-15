import numpy as np

a = [['B', 'C', 'C', 'C', 'A', 'C', 'C', 'B'], ['C', 'A', 'B', 'C', 'A', 'C', 'A', 'B'], ['B', 'A', 'A', 'C', 'C', 'C', 'A', 'C'], ['B', 'B', 'A', 'B', 'B', 'A', 'B', 'C'], [
    'C', 'C', 'A', 'B', 'A', 'B', 'C', 'A'], ['C', 'A', 'B', 'A', 'B', 'A', 'C', 'C'], ['C', 'B', 'A', 'C', 'A', 'C', 'A', 'B'], ['C', 'B', 'C', 'C', 'C', 'B', 'A', 'B']]

print(a)


b = np.array(a).T

print(b)
