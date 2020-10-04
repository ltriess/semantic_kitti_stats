# -*- coding: utf-8 -*-

__author__ = """Larissa Triess"""
__email__ = "larissa@triess.eu"

import numpy as np
from data import azimuth_bins, distance_bins, elevation_bins, get_num_learning_labels


def get_counts(
    data: np.array,
    labels: np.array,
    restriction_1: int,
    restriction_bins_2: np.array,
    lower: bool = False,
):

    off = 0
    if lower:
        off = 1
    counter = np.zeros(
        [restriction_1, restriction_bins_2.shape[0] + off], dtype=np.int64
    )
    for l in range(restriction_1):

        # remove all points that are not of current label
        depth_current_label = data[labels == l]

        if lower:
            r = (-1, restriction_bins_2.shape[0])
        else:
            r = (0, restriction_bins_2.shape[0])
        for b in range(*r):
            if b == -1:
                bin_min = -np.inf
                bin_max = restriction_bins_2[b + 1]
            elif b == len(restriction_bins_2) - 1:
                bin_min = restriction_bins_2[b]
                bin_max = np.inf
            else:
                bin_min = restriction_bins_2[b]
                bin_max = restriction_bins_2[b + 1]

            counter[l, b + off] = np.sum(
                np.logical_and(
                    np.where(
                        np.greater_equal(depth_current_label, bin_min), True, False
                    ),
                    np.where(np.less(depth_current_label, bin_max), True, False),
                )
            )

    return counter


def get_points_over_distance_and_label_statistics(
    coordinates: np.array, labels: np.array
) -> (np.array, np.array, np.array):

    depth = np.linalg.norm(coordinates, 2, axis=1)
    labels = labels[:, 0]

    counter = get_counts(
        depth, labels, get_num_learning_labels(), np.array(distance_bins)
    )

    return np.sum(counter, axis=0), np.sum(counter, axis=1), counter


def get_points_over_angles_and_label_statistics(
    coordinates: np.array, labels: np.array
) -> (np.array, np.array):

    azimuth = np.arctan2(coordinates[:, 1], coordinates[:, 0])  # [-pi, pi]
    azimuth = np.mod(np.add(azimuth, 2 * np.pi), 2 * np.pi)  # [0, 2pi]
    elevation = np.arccos(
        np.true_divide(coordinates[:, 2], np.linalg.norm(coordinates, 2, axis=1))
    )  # [0, pi]
    elevation = np.where(
        elevation > np.pi / 2, -np.mod(elevation, np.pi / 2), elevation
    )  # [- pi/2, pi/2]
    labels = labels[:, 0]

    counter_a = get_counts(
        azimuth,
        labels,
        get_num_learning_labels(),
        np.multiply(azimuth_bins, np.pi / 180),
    )
    counter_e = get_counts(
        elevation,
        labels,
        get_num_learning_labels(),
        np.multiply(elevation_bins, np.pi / 180),
        lower=True,
    )

    return counter_a, counter_e
