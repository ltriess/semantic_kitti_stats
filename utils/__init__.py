# -*- coding: utf-8 -*-

__author__ = """Larissa Triess"""
__email__ = 'larissa@triess.eu'

from .compute import get_points_over_distance_and_label_statistics as get_distance_label_stats
from .compute import get_points_over_angles_and_label_statistics as get_angle_label_stats

__all__ = [
    'get_distance_label_stats',
    'get_angle_label_stats',
]
