#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Separate analysis of Semantic KITTI sequences and total statistics."""

__author__ = """Larissa Triess"""
__email__ = "larissa@triess.eu"

import os
import sys

import click
import numpy as np
from data import (
    azimuth_bins,
    distance_bins,
    elevation_bins,
    get_num_learning_labels,
    load_data_labels,
    load_data_points,
    map_learning,
)
from utils import get_angle_label_stats, get_distance_label_stats, plots


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option(
    "--mode",
    type=click.Choice(["compute", "from_data"]),
    default="compute",
    help="If compute is selected, PATH must be the path to the dataset. All statistics "
    "will be calculated from the data. If from_data is selected, PATH must be a "
    "a folder in which csv files with the computed statistics are located.",
)
@click.option(
    "--save_dir",
    type=click.Path(dir_okay=True),
    help="Path where to save the generated graphs. If not provided, show on display.",
)
def analyse(path, mode, save_dir):

    sequence_folder = os.path.join(path, "dataset", "sequences")

    # placeholder for overall stats
    pplds = np.zeros(
        [11, get_num_learning_labels(), len(distance_bins)], dtype=np.int64
    )

    # iterate over all train/val sequences
    for s in range(11):
        if mode == "compute":
            print("\nSequence {seq}".format(seq=s))

            point_dir = os.path.join(sequence_folder, "{0:02d}".format(s), "velodyne")
            label_dir = os.path.join(sequence_folder, "{0:02d}".format(s), "labels")

            if not os.path.exists(point_dir):
                raise NotADirectoryError(
                    "Directory for points does not exits: {dir}".format(dir=point_dir)
                )
            if not os.path.exists(label_dir):
                raise NotADirectoryError(
                    "Directory for labels does not exits: {dir}".format(dir=label_dir)
                )
            if save_dir is not None and not os.path.exists(save_dir):
                os.makedirs(save_dir)

            points_per_distance = np.zeros(len(distance_bins), dtype=np.int64)
            points_per_label = np.zeros(get_num_learning_labels(), dtype=np.int64)
            points_per_label_distance = np.zeros(
                [get_num_learning_labels(), len(distance_bins)], dtype=np.int64
            )
            points_per_label_azimuth = np.zeros(
                [get_num_learning_labels(), len(azimuth_bins)], dtype=np.int64
            )
            points_per_label_elevation = np.zeros(
                [get_num_learning_labels(), len(elevation_bins) + 1], dtype=np.int64
            )

            point_filenames = sorted(os.listdir(point_dir))
            label_filenames = sorted(os.listdir(label_dir))
            for c, (point_file, label_file) in enumerate(
                zip(point_filenames, label_filenames)
            ):
                sys.stdout.write("\r{0:4d} / {1:4d}".format(c, len(point_filenames)))

                point_filename = os.path.join(point_dir, point_file)
                label_filename = os.path.join(label_dir, label_file)

                if (
                    not os.path.splitext(point_file)[0]
                    == os.path.splitext(label_file)[0]
                ):
                    raise ValueError(
                        "Point list file {pf} does not match label file {lf}".format(
                            pf=point_filename, lf=label_filename
                        )
                    )

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
                np.savetxt(
                    os.path.join(save_dir, "{0:02d}_points_per_distance.csv".format(s)),
                    points_per_distance,
                    delimiter=",",
                )
                np.savetxt(
                    os.path.join(save_dir, "{0:02d}_points_per_label.csv".format(s)),
                    points_per_label,
                    delimiter=",",
                )
                np.savetxt(
                    os.path.join(
                        save_dir, "{0:02d}_distance_label_matrix.csv".format(s)
                    ),
                    points_per_label_distance,
                    delimiter=",",
                )
                np.savetxt(
                    os.path.join(
                        save_dir, "{0:02d}_azimuth_label_matrix.csv".format(s)
                    ),
                    points_per_label_azimuth,
                    delimiter=",",
                )
                np.savetxt(
                    os.path.join(
                        save_dir, "{0:02d}_elevation_label_matrix.csv".format(s)
                    ),
                    points_per_label_elevation,
                    delimiter=",",
                )

        elif mode == "from_data":
            points_per_distance = np.loadtxt(
                os.path.join(path, "{0:02d}_points_per_distance.csv".format(s)),
                delimiter=",",
            )
            points_per_label = np.loadtxt(
                os.path.join(path, "{0:02d}_points_per_label.csv".format(s)),
                delimiter=",",
            )
            points_per_label_distance = np.loadtxt(
                os.path.join(path, "{0:02d}_distance_label_matrix.csv".format(s)),
                delimiter=",",
            )
            points_per_label_azimuth = np.loadtxt(
                os.path.join(path, "{0:02d}_azimuth_label_matrix.csv".format(s)),
                delimiter=",",
            )
            points_per_label_elevation = np.loadtxt(
                os.path.join(path, "{0:02d}_elevation_label_matrix.csv".format(s)),
                delimiter=",",
            )
        else:
            raise ValueError

        pplds[s] = points_per_label_distance

        # visualize the data
        plots.draw_distance_and_label_matrix(
            points_per_label_distance,
            save_dir=os.path.join(save_dir, "{0:02d}_distance_label_matrix".format(s))
            if save_dir is not None
            else None,
        )
        plots.draw_points_per_distance(
            points_per_distance,
            save_dir=os.path.join(save_dir, "{0:02d}_points_per_distance.".format(s))
            if save_dir is not None
            else None,
        )
        plots.draw_points_per_label(
            points_per_label,
            save_dir=os.path.join(save_dir, "{0:02d}_points_per_label".format(s))
            if save_dir is not None
            else None,
        )
        plots.draw_azimuth_and_label_matrix(
            points_per_label_azimuth,
            save_dir=os.path.join(save_dir, "{0:02d}_azimuth_label_matrix".format(s))
            if save_dir is not None
            else None,
        )
        plots.draw_elevation_and_label_matrix(
            points_per_label_elevation,
            save_dir=os.path.join(save_dir, "{0:02d}_elevation_label_matrix".format(s))
            if save_dir is not None
            else None,
        )

    print("\n")
    print("Finished all sequences. Starting total analysis...")

    ppld = np.sum(pplds, axis=0)  # total points per label distance
    ppl = np.sum(ppld, axis=1)  # total points per label
    ppd = np.sum(ppld, axis=0)  # total points per distance

    ppds = np.sum(pplds, axis=1)  # points per distance sequence
    ppls = np.sum(pplds, axis=2)  # points per label sequence

    # save the data
    if save_dir is not None:
        np.savetxt(
            os.path.join(save_dir, "total_distance_label_matrix.csv"),
            ppld,
            delimiter=",",
        )
        np.savetxt(
            os.path.join(save_dir, "total_points_per_distance.csv"), ppd, delimiter=","
        )
        np.savetxt(
            os.path.join(save_dir, "total_points_per_label.csv"), ppl, delimiter=","
        )

        np.savetxt(
            os.path.join(save_dir, "sequence_distance_matrix.csv"), ppds, delimiter=","
        )
        np.savetxt(
            os.path.join(save_dir, "sequence_label_matrix.csv"), ppls, delimiter=","
        )

    # visualize the data
    plots.draw_distance_and_label_matrix(
        ppld,
        save_dir=os.path.join(save_dir, "total_distance_label_matrix")
        if save_dir is not None
        else None,
    )
    plots.draw_points_per_distance(
        ppd,
        save_dir=os.path.join(save_dir, "total_points_per_distance")
        if save_dir is not None
        else None,
    )
    plots.draw_points_per_label(
        ppl,
        save_dir=os.path.join(save_dir, "total_points_per_label")
        if save_dir is not None
        else None,
    )

    plots.draw_distance_and_sequence_matrix(
        ppds,
        save_dir=os.path.join(save_dir, "sequence_distance_matrix")
        if save_dir is not None
        else None,
    )
    plots.draw_label_and_sequence_matrix(
        ppls,
        save_dir=os.path.join(save_dir, "sequence_label_matrix")
        if save_dir is not None
        else None,
    )
    plots.draw_sequence_length(
        save_dir=os.path.join(path, "sequence_length") if save_dir is not None else None
    )


if __name__ == "__main__":
    analyse()
