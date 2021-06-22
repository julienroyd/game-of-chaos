import numpy as np

def sample_point(init_points, last_point):
    ref_point = init_points[np.random.randint(low=0, high=len(init_points))]
    new_point = np.mean([ref_point, last_point], axis=0)
    return new_point