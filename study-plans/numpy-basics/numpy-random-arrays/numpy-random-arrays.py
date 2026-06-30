import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """

    # for some reason, this test does not support the modern implementation

    np.random.seed(seed)
    if kind == 'uniform':
        return np.random.random(shape)
    if kind == 'normal':
        return np.random.standard_normal(shape)
