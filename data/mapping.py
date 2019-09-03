# -*- coding: utf-8 -*-

__author__ = """Larissa Triess"""
__email__ = 'larissa@triess.eu'

import numpy as np


label_names = [
    [0, 'unlabeled'], [1, 'outlier'], [10, 'car'], [11, 'bicycle'], [13, 'bus'], [15, 'motorcycle'],
    [16, 'on-rails'], [18, 'truck'], [20, 'other-vehicle'], [30, 'person'], [31, 'bicyclist'],
    [32, 'motorcyclist'], [40, 'road'], [44, 'parking'], [48, 'sidewalk'], [49, 'other-ground'],
    [50, 'building'], [51, 'fence'], [52, 'other-structure'], [60, 'lane-marking'],
    [70, 'vegetation'], [71, 'trunk'], [72, 'terrain'], [80, 'pole'], [81, 'traffic-sign'],
    [99, 'other-object'], [252, 'moving-car'], [253, 'moving-bicyclist'], [254, 'moving-person'],
    [255, 'moving-motorcyclist'], [256, 'moving-on-rails'], [257, 'moving-bus'],
    [258, 'moving-truck'], [259, 'moving-other-vehicle'],
]
label_mapping = [
    [0, 0], [1, 0], [10, 1], [11, 2], [13, 5], [15, 3], [16, 5], [18, 4], [20, 5], [30, 6],
    [31, 7], [32, 8], [40, 9], [44, 10], [48, 11], [49, 12], [50, 13], [51, 14], [52, 0],
    [60, 9], [70, 15], [71, 16], [72, 17], [80, 18], [81, 19], [99, 0], [252, 1], [253, 7],
    [254, 6], [255, 8], [256, 5], [257, 5], [258, 4], [259, 5],
]


def get_num_learning_labels() -> int:
    return len(np.unique(np.array(label_mapping)[:, 1]))


def get_names_learning() -> (np.array, np.array, np.array):
    """ Return the label names, the label ids while training, the label ids of the file
    """
    mapping = np.array(label_mapping)
    uniques, indices = np.unique(mapping[:, 1], return_index=True)
    labels_relevant = mapping[:, 0][indices]
    names = [label_names[i][1] for i in indices]
    return names, uniques, labels_relevant


def map_learning(labels: np.array) -> np.array:
    old = np.array(label_mapping)[:, 0]
    new = np.array(label_mapping)[:, 1]

    output = np.copy(labels)
    for o, n in zip(old, new):
        output[labels == o] = n
    return output
