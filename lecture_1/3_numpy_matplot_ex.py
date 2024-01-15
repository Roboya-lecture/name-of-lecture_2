import numpy as np
import matplotlib.pyplot as plt

A, B = 3, -5
def function_1D(x, a, b, noise=False):
  y = a*x + b
  y += (np.random.random()-0.5)*10 if noise else 0
  return y


X = [np.random.randint(30) for i in range(10)]
Y = []
for x in X:
  y = function_1D(x, A, B, True)
  Y.append(y)

A = np.vstack([X, np.ones(len(X))]).T
m, c = np.linalg.lstsq(A, Y, rcond=None)[0]
print(m, c)

fit_Y = []
for x in X:
  y = function_1D(x, m, c)
  fit_Y.append(y)

plt.plot(X, Y, 'ro')
plt.plot(X,fit_Y)
plt.show()
