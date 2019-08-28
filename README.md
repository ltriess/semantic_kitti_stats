# Semantic KITTI Dataset Statistics

This repository holds a script that allows an analysis of the [Semantic KITTI Dataset](http://semantic-kitti.org/) [1,2].
The main focus is on distance and label analysis.
For all statistics a csv file and a plot are generated.

Some Examples:
* see which label has how many points over the distance

![teaser1](/figures/total_distance_label_matrix.png)

* see how many points belong to a specific label in each sequence

![teaser2](/figures/sequence_label_matrix.png)


* ... and many more, such as the analysis per sequence or labels over azimuth and elevation angle


## Contents
* [Getting Started](#getting-started)
* [Running the code](#running-the-code)
* [License](#license)
* [References](#references)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installing

```
$ git clone https://github.com/ltriess/semantic_kitti_stats.git
$ cd semantic_kitti_stats
$ pip install requirements.txt
```

### Get the Data

Download the data and unzip it in the same folder.
* for the labels: [Semantic KITTI](http://semantic-kitti.org/dataset.html#download)
* for the point clouds: [KITTI Odometry](http://www.cvlibs.net/datasets/kitti/eval_odometry.php)

## Running the code

The main script is `analyse.py` which can be called according to

```
Usage: analyse_sequence.py [OPTIONS] PATH

Options:
  --mode [compute|from_data]  If compute is selected, PATH must be the path to the dataset.
                              All statistics will be calculated from the data. If from_data
                              is selected, PATH must be a a folder in which csv files with
                              the computed statistics are located.
  --save_dir PATH             Path where to save the generated graphs. If not provided, show on display.
  --help                      Show this message and exit.
```

The script first iterates over all trainval sequences and generates separate statistics for each sequence.
Finally, all the sequence statistics are combined and a total analysis as well as a sequence overview is generated.
There are two modes in which the script dan be called:

* _compute_: PATH must point to the root directory of the dataset which contains the folders
dataset/sequences/{00..10}/{velodyne/labels} according to how the dataset is extracted after the download.
All statistics will be computed from the dataset and then plots will be generated.
If _save_dir_ is set to a valid path, all the statistics will be saved to csv files for later usage.
* _from_data_: PATH must point to the folder in which all the generated csv files are located.
This is useful when the statistics are available, but a redo of the plots is needed.

In both modes, if _save_dir_ is set, the plots are saved as png files to the specified location.
If it is not set, the plots will be displayed on the screen.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## References
[1] J. Behley and M. Garbade and A. Milioto and J. Quenzel and S. Behnke and C. Stachniss and J. Gall, 
"SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences", ICCV 2019

[2] A. Geiger and P. Lenz and C. Stiller and R. Urtasun, Vision meets Robotics: The KITTI Dataset, IJRR 2013
