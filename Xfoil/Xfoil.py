import numpy as np
import pandas as pd

def download_file(app, dataBuffer):
    # Boundary point X-coordinate
    X = dataBuffer[:,0]
    # Boundary point Y-coordinate
    Y = dataBuffer[:,1]
    
    datapoints = pd.DataFrame({'x': X, 'y': Y})
    
    app.logger.info('Downloaded file')
    
    return datapoints