# -*- coding: utf-8 -*-

__author__ = """Larissa Triess"""
__email__ = "larissa@triess.eu"

import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
from data import (
    azimuth_bins,
    distance_bins,
    elevation_bins,
    get_names_learning,
    get_num_learning_labels,
)


def draw_distance_and_label_matrix(matrix: np.array, save_dir: str = None):
    class_names, _, _ = get_names_learning()

    fig, ax = plt.subplots()
    im = ax.pcolor(
        matrix, norm=colors.LogNorm(vmin=1, vmax=np.max(matrix)), cmap=plt.cm.Blues
    )
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Number of Points", rotation=90)

    ax.set_xlabel("Distance [m]")
    ax.set_xticks(np.arange(matrix.shape[1]))
    ax.set_xticklabels(distance_bins, ha="right", rotation=45, rotation_mode="anchor")
    ax.xaxis.set_label_position("bottom")
    ax.xaxis.tick_bottom()

    ax.set_ylabel("Class Label")
    ax.set_yticks(np.arange(matrix.shape[0] + 1))
    ax.set_yticklabels(class_names, va="bottom")
    ax.yaxis.set_label_position("left")
    ax.yaxis.tick_left()

    plt.tight_layout()

    if save_dir is None:
        plt.show()
    else:
        plt.savefig(save_dir)
        plt.close()


def draw_azimuth_and_label_matrix(matrix: np.array, save_dir: str = None):
    class_names, _, _ = get_names_learning()

    fig, ax = plt.subplots()
    im = ax.pcolor(
        matrix, norm=colors.LogNorm(vmin=1, vmax=np.max(matrix)), cmap=plt.cm.Blues
    )
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Number of Points", rotation=90)

    ax.set_xlabel("Azimuth [degree]")
    ax.set_xticks(np.arange(matrix.shape[1] + 1))
    ax.set_xticklabels(
        np.append(azimuth_bins, 360), ha="right", rotation=45, rotation_mode="anchor"
    )
    ax.xaxis.set_label_position("bottom")
    ax.xaxis.tick_bottom()
    for i, l in enumerate(ax.xaxis.get_ticklabels()):
        if i % 4 == 0:
            l.set_visible(True)
        else:
            l.set_visible(False)

    ax.set_ylabel("Class Label")
    ax.set_yticks(np.arange(matrix.shape[0] + 1))
    ax.set_yticklabels(class_names, va="bottom")
    ax.yaxis.set_label_position("left")
    ax.yaxis.tick_left()

    plt.tight_layout()

    if save_dir is None:
        plt.show()
    else:
        plt.savefig(save_dir)
        plt.close()


def draw_elevation_and_label_matrix(matrix: np.array, save_dir: str = None):
    class_names, _, _ = get_names_learning()

    fig, ax = plt.subplots()
    im = ax.pcolor(
        matrix, norm=colors.LogNorm(vmin=1, vmax=np.max(matrix)), cmap=plt.cm.Blues
    )
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Number of Points", rotation=90)

    ax.set_xlabel("Elevation [degree]")
    ax.set_xticks(np.arange(matrix.shape[1]))
    ax.set_xticklabels(elevation_bins, ha="right", rotation=45, rotation_mode="anchor")
    ax.xaxis.set_label_position("bottom")
    ax.xaxis.tick_bottom()
    for i, l in enumerate(ax.xaxis.get_ticklabels()):
        if i % 4 == 0:
            l.set_visible(True)
        else:
            l.set_visible(False)

    ax.set_ylabel("Class Label")
    ax.set_yticks(np.arange(matrix.shape[0] + 1))
    ax.set_yticklabels(class_names, va="bottom")
    ax.yaxis.set_label_position("left")
    ax.yaxis.tick_left()

    plt.tight_layout()

    if save_dir is None:
        plt.show()
    else:
        plt.savefig(save_dir)
        plt.close()


def draw_points_per_distance(ppd: np.array, save_dir: str = None):

    fig, ax = plt.subplots()
    plt.bar(np.arange(len(distance_bins)), ppd)

    ax.set_xlabel("Distance [m]")
    ax.set_xticks(np.arange(len(distance_bins)) - 0.5)
    ax.set_xticklabels(distance_bins)

    plt.ylabel("Number of Points")
    plt.yscale("log")

    plt.tight_layout()

    if save_dir is None:
        plt.show()
    else:
        plt.savefig(save_dir)
        plt.close()


def draw_points_per_label(ppl: np.array, save_dir: str = None):

    fig, ax = plt.subplots()
    plt.bar(np.arange(get_num_learning_labels()), ppl)

    ax.set_xlabel("Class Label")
    ax.set_xticks(np.arange(get_num_learning_labels()))
    ax.set_xticklabels(
        get_names_learning()[0], ha="right", rotation=45, rotation_mode="anchor"
    )

    plt.ylabel("Number of Points")
    plt.yscale("log")

    plt.tight_layout()

    if save_dir is None:
        plt.show()
    else:
        plt.savefig(save_dir)
        plt.close()


def draw_distance_and_sequence_matrix(matrix: np.array, save_dir: str = None):

    fig, ax = plt.subplots()
    im = ax.pcolor(
        matrix.T, norm=colors.LogNorm(vmin=1, vmax=np.max(matrix)), cmap=plt.cm.Blues
    )
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Number of Points", rotation=90)

    ax.set_xlabel("Sequence")
    ax.set_xticks(np.arange(matrix.shape[0]))
    ax.set_xticklabels(["{i:02d}".format(i=i) for i in range(11)], ha="center")
    ax.set_xticks([float(n) + 0.5 for n in ax.get_xticks()])
    ax.xaxis.set_label_position("bottom")
    ax.xaxis.tick_bottom()

    ax.set_ylabel("Distance [m]")
    ax.set_yticks(np.arange(matrix.shape[1] + 1))
    ax.set_yticklabels(distance_bins, va="center")
    ax.yaxis.set_label_position("left")
    ax.yaxis.tick_left()

    plt.tight_layout()

    if save_dir is None:
        plt.show()
    else:
        plt.savefig(save_dir)
        plt.close()


def draw_label_and_sequence_matrix(matrix: np.array, save_dir: str = None):
    class_names, _, _ = get_names_learning()

    fig, ax = plt.subplots()
    im = ax.pcolor(
        matrix.T, norm=colors.LogNorm(vmin=1, vmax=np.max(matrix)), cmap=plt.cm.Blues
    )
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Number of Points", rotation=90)

    ax.set_xlabel("Sequence")
    ax.set_xticks(np.arange(matrix.shape[0]))
    ax.set_xticklabels(["{i:02d}".format(i=i) for i in range(11)], ha="center")
    ax.set_xticks([float(n) + 0.5 for n in ax.get_xticks()])
    ax.xaxis.set_label_position("bottom")
    ax.xaxis.tick_bottom()

    ax.set_ylabel("Class Label")
    ax.set_yticks(np.arange(matrix.shape[1] + 1))
    ax.set_yticklabels(class_names, va="bottom")
    ax.yaxis.set_label_position("left")
    ax.yaxis.tick_left()

    plt.tight_layout()

    if save_dir is None:
        plt.show()
    else:
        plt.savefig(save_dir)
        plt.close()


def draw_sequence_length(save_dir: str = None):
    length = [
        4541,
        1101,
        4661,
        801,
        271,
        2661,
        1101,
        1101,
        4071,
        1591,
        1201,
        921,
        1061,
        3281,
        631,
        1901,
        1731,
        491,
        1801,
        4981,
        831,
        2721,
    ]

    fig, ax = plt.subplots()
    barlist = plt.bar(np.arange(22), length)

    ax.set_xlabel("Sequence")
    ax.set_xticks(np.arange(22))
    ax.set_xticklabels(["{i:02d}".format(i=i) for i in range(22)], ha="center")

    plt.ylabel("Number of Frames")

    barlist[8].set_color("m")
    for i in range(11, 22):
        barlist[i].set_color("c")

    plt.legend((barlist[0], barlist[8], barlist[11]), ("train", "val", "test"))

    plt.tight_layout()

    if save_dir is None:
        plt.show()
    else:
        plt.savefig(save_dir)
        plt.close()
