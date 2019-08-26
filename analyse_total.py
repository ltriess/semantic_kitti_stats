#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Fuse the per sequence statistics to get an overall analysis."""

import os

import numpy as np
import click

from data import distance_bins, get_num_learning_labels
from utils import plots


__author__ = "Larissa Triess"
__copyright__ = "Copyright 2019, Larissa Triess"
__license__ = "MIT"
__version__ = "0.1.0"


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--mode', type=click.Choice(['from_folder', 'from_files']),
              help='If from_folder is selected, PATH must contain all csv files of the single'
                   'sequences. All statistics will be calculated from the data. If from_files is '
                   'selected, DIR must be a path to a folder where csv files with the combined '
                   'computed statistics are located.')
@click.option('--save', is_flag=True, help='If True, save to PATH.')
def combine(path, mode, save):

    if mode == 'from_folder':
        pplds = np.zeros([11, get_num_learning_labels(), len(distance_bins)], dtype=np.int64)
        for i in range(11):
            pplds[i] = np.int64(np.loadtxt(
                os.path.join(path, '{:02d}_distance_label_matrix.csv'.format(i)), delimiter=','))

        # total points per label distance
        ppld = np.sum(pplds, axis=0)
        # total points per label
        ppl = np.sum(ppld, axis=1)
        # total points per distance
        ppd = np.sum(ppld, axis=0)

        # points per distance sequence
        ppds = np.sum(pplds, axis=1)
        # points per label sequence
        ppls = np.sum(pplds, axis=2)

        # save the data
        if save:
            np.savetxt(os.path.join(path, 'total_distance_label_matrix.csv'), ppld, delimiter=',')
            np.savetxt(os.path.join(path, 'total_points_per_distance.csv'), ppd, delimiter=',')
            np.savetxt(os.path.join(path, 'total_points_per_label.csv'), ppl, delimiter=',')

            np.savetxt(os.path.join(path, 'sequence_distance_matrix.csv'), ppds, delimiter=',')
            np.savetxt(os.path.join(path, 'sequence_label_matrix.csv'), ppls, delimiter=',')

    elif mode == 'from_files':
        ppld = np.loadtxt(os.path.join(path, 'total_distance_label_matrix.csv'), delimiter=',')
        ppd = np.loadtxt(os.path.join(path, 'total_points_per_distance.csv'), delimiter=',')
        ppl = np.loadtxt(os.path.join(path, 'total_points_per_label.csv'), delimiter=',')

        ppds = np.loadtxt(os.path.join(path, 'sequence_distance_matrix.csv'), delimiter=',')
        ppls = np.loadtxt(os.path.join(path, 'sequence_label_matrix.csv'), delimiter=',')

    else:
        raise ValueError

    # visualize the data
    plots.draw_distance_and_label_matrix(
        ppld, save_dir=os.path.join(path, 'total_distance_label_matrix') if save else None)
    plots.draw_points_per_distance(
        ppd, save_dir=os.path.join(path, 'total_points_per_distance') if save else None)
    plots.draw_points_per_label(
        ppl, save_dir=os.path.join(path, 'total_points_per_label') if save else None)

    plots.draw_distance_and_sequence_matrix(
        ppds, save_dir=os.path.join(path, 'sequence_distance_matrix') if save else None)
    plots.draw_label_and_sequence_matrix(
        ppls, save_dir=os.path.join(path, 'sequence_label_matrix') if save else None)
    plots.draw_sequence_length(save_dir=os.path.join(path, 'sequence_length') if save else None)


if __name__ == '__main__':
    combine()
