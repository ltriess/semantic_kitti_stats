# -*- coding: utf-8 -*-

__author__ = """Larissa Triess"""
__email__ = "larissa@triess.eu"

import numpy as np


def load_data_points(path: str) -> (np.array, np.array):
    cloud = np.fromfile(path, dtype=np.float32).reshape((-1, 4))
    return cloud[:, :-1], cloud[:, -1][:, np.newaxis]


def load_data_labels(path: str) -> (np.array, np.array):
    labels = np.fromfile(path, dtype=np.uint32).reshape((-1, 1))
    return labels & 0xFFFF, labels >> 16
