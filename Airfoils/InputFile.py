import numpy as np
import pandas as pd

def compute_input_file(dataBuffer):
    # Boundary point X-coordinate
    X = dataBuffer[:,0]
    # Boundary point Y-coordinate
    Y = dataBuffer[:,1]
    
    print(X)
    
    print("=" * 40)
    
    print(Y)
    
    datapoints = pd.DataFrame({'x': X, 'y': Y})
    
    print(datapoints)
    
    return datapoints