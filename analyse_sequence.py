#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Separate analysis of Semantic KITTI sequences."""

import os
import sys

import numpy as np
import click

from data import distance_bins, azimuth_bins, elevation_bins, load_data_points, load_data_labels, \
    get_num_learning_labels, map_learning
from utils import plots, get_distance_label_stats, get_angle_label_stats


__author__ = "Larissa Triess"
__copyright__ = "Copyright 2019, Larissa Triess"
__license__ = "MIT"
__version__ = "0.1.0"


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--mode', type=click.Choice(['from_sequence', 'from_data']),
              help='If from_sequence is selected, PATH must be a path to a sequence. All statistics '
                   'will be calculated from the data. If from_data is selected, DIR must be a '
                   'path to a folder where csv files with the computed statistics are located.')
@click.option('--save_dir', type=click.Path(dir_okay=True), default=None,
              help='Path where to save the generated graphs. If not provided, show on display.')
def analyse(path, mode, save_dir):

    s_id = os.path.basename(path.rstrip('/'))

    if mode == 'from_sequence':
        point_dir = os.path.join(path, 'velodyne')
        label_dir = os.path.join(path, 'labels')

        if not os.path.exists(point_dir):
            raise NotADirectoryError('Directory for points does not exits: {}'.format(point_dir))
        if not os.path.exists(label_dir):
            raise NotADirectoryError('Directory for labels does not exits: {}'.format(label_dir))
        if save_dir is not None:
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

        points_per_distance = np.zeros(len(distance_bins), dtype=np.int64)
        points_per_label = np.zeros(get_num_learning_labels(), dtype=np.int64)
        points_per_label_distance = np.zeros(
            [get_num_learning_labels(), len(distance_bins)], dtype=np.int64)
        points_per_label_azimuth = np.zeros(
            [get_num_learning_labels(), len(azimuth_bins)], dtype=np.int64)
        points_per_label_elevation = np.zeros(
            [get_num_learning_labels(), len(elevation_bins) + 1], dtype=np.int64)

        point_filenames = sorted(os.listdir(point_dir))
        label_filenames = sorted(os.listdir(label_dir))
        for c, (point_file, label_file) in enumerate(zip(point_filenames, label_filenames)):
            sys.stdout.write('\r{:4d} / {:4d}'.format(c, len(point_filenames)))

            point_filename = os.path.join(point_dir, point_file)
            label_filename = os.path.join(label_dir, label_file)

            if not os.path.splitext(point_file)[0] == os.path.splitext(label_file)[0]:
                raise ValueError('Point list file {} does not match label file {}'.format(
                    point_filename, label_filename))

            sensor, intensity = load_data_points(point_filename)
            semantics, instance = load_data_labels(label_filename)

            semantics = map_learning(semantics)
            ppd, ppl, ppld = get_distance_label_stats(sensor, semantics)
            ppla, pple = get_angle_label_stats(sensor, semantics)

            points_per_distance = np.add(points_per_distance, ppd)
            points_per_label = np.add(points_per_label, ppl)
            points_per_label_distance = np.add(points_per_label_distance, ppld)
            points_per_label_azimuth = np.add(points_per_label_azimuth, ppla)
            points_per_label_elevation = np.add(points_per_label_elevation, pple)

        # save the data
        if save_dir is not None:
            np.savetxt(os.path.join(save_dir, '{}_points_per_distance.csv'.format(s_id)),
                       points_per_distance, delimiter=',')
            np.savetxt(os.path.join(save_dir, '{}_points_per_label.csv'.format(s_id)),
                       points_per_label, delimiter=',')
            np.savetxt(os.path.join(save_dir, '{}_distance_label_matrix.csv'.format(s_id)),
                       points_per_label_distance, delimiter=',')
            np.savetxt(os.path.join(save_dir, '{}_azimuth_label_matrix.csv'.format(s_id)),
                       points_per_label_azimuth, delimiter=',')
            np.savetxt(os.path.join(save_dir, '{}_elevation_label_matrix.csv'.format(s_id)),
                       points_per_label_elevation, delimiter=',')

    elif mode == 'from_data':
        points_per_distance = np.loadtxt(
            os.path.join(path, '{}_points_per_distance.csv'.format(s_id)), delimiter=',')
        points_per_label = np.loadtxt(
            os.path.join(path, '{}_points_per_label.csv'.format(s_id)), delimiter=',')
        points_per_label_distance = np.loadtxt(
            os.path.join(path, '{}_distance_label_matrix.csv'.format(s_id)), delimiter=',')
        points_per_label_azimuth = np.loadtxt(
            os.path.join(path, '{}_azimuth_label_matrix.csv'.format(s_id)), delimiter=',')
        points_per_label_elevation = np.loadtxt(
            os.path.join(path, '{}_elevation_label_matrix.csv'.format(s_id)), delimiter=',')
    else:
        raise ValueError

    # visualize the data
    plots.draw_distance_and_label_matrix(
        points_per_label_distance,
        save_dir=os.path.join(save_dir, '{}_distance_label_matrix'.format(s_id))
        if save_dir is not None else None)
    plots.draw_points_per_distance(
        points_per_distance,
        save_dir=os.path.join(save_dir, '{}_points_per_distance.'.format(s_id))
        if save_dir is not None else None)
    plots.draw_points_per_label(
        points_per_label,
        save_dir=os.path.join(save_dir, '{}_points_per_label'.format(s_id))
        if save_dir is not None else None)
    plots.draw_azimuth_and_label_matrix(
        points_per_label_azimuth,
        save_dir=os.path.join(save_dir, '{}_azimuth_label_matrix'.format(s_id))
        if save_dir is not None else None)
    plots.draw_elevation_and_label_matrix(
        points_per_label_elevation,
        save_dir=os.path.join(save_dir, '{}_elevation_label_matrix'.format(s_id))
        if save_dir is not None else None)


if __name__ == '__main__':
    analyse()
