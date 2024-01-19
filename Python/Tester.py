import numpy as np
from naca4 import computeNacaAirfoil
import pandas as pd

text, xu, yu, xl, yl = computeNacaAirfoil(2, 4, 12, 10)

x = np.append(xu, xl)
y = np.append(yu, yl)
print(x)
print(y)

df = pd.DataFrame({'x': x, 'y': y})