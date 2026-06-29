import numpy as np

def create_filled_array(shape, kind):
    """
    Returns: 2D numpy array of given shape with dtype float64
    """
    n, m = shape[0], shape[1]
    
    if kind == 'zeros':
        return np.zeros((n, m), dtype='float64')
    if kind == 'ones':
        return np.ones((n, m), dtype='float64')