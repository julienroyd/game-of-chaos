import numpy as np

def sample_point(init_points, last_point, ref_weight=0.5):
    ref_point = init_points[np.random.randint(low=0, high=len(init_points))]
    new_point = ref_weight * ref_point + (1 - ref_weight) * last_point
    return new_point