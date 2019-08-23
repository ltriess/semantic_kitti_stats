# -*- coding: utf-8 -*-

import numpy as np

from .loader import load_data_points, load_data_labels
from .mapping import get_num_learning_labels, get_names_learning, map_learning

distance_bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
azimuth_bins = np.linspace(start=0, stop=360, num=36, endpoint=False, dtype=np.int64)
elevation_bins = [-25.0761, -24.5066, -24.0199, -23.4507, -22.8068, -22.4876, -22.0664, -21.5110,
                  -20.9104, -20.3256, -19.8608, -19.4036, -18.8810, -18.3656, -17.7410, -17.2830,
                  -16.6938, -16.3493, -15.7978, -15.2760, -14.7296, -14.2685, -13.5955, -13.1965,
                  -12.7294, -12.2828, -11.7450, -11.1826, -10.4821, -10.1420, -9.6304, -9.1631,
                  -8.7000, -8.3105, -7.9776, -7.6328, -7.2758, -6.9760, -6.6411, -6.2595, -5.9120,
                  -5.5874, -5.2624, -4.9022, -4.5997, -4.2621, -3.9359, -3.5627, -3.2009, -2.8855,
                  -2.5349, -2.2310, -1.8449, -1.5641, -1.2012, -0.8617, -0.5455, -0.1590, 0.1338,
                  0.4968, 0.8950, 1.1877, 1.5037, 1.8665]


__all__ = [
    'distance_bins',
    'azimuth_bins',
    'elevation_bins',
    'load_data_points',
    'load_data_labels',
    'get_num_learning_labels',
    'get_names_learning',
    'map_learning',
]
