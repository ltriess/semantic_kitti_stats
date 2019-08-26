# Semantic KITTI Dataset Statistics

This repository contains two scripts that allow an analysis of the 
[Semantic KITTI Dataset](http://semantic-kitti.org/) [1,2] and creates some plots.

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

There are two different scripts: `analyse_total.py` can only be run when the data was previously generated with `analyse_sequence.py`.
The latter one gives separate analysis of all trainval sequences.
A total evaluation based on the computed per sequence statistics can be generated with the first script.

`analyse_sequence.py` can be called with the path to the root directory of the dataset if _mode_ is selected as _compute_.
The root directory contains the folders dataset/sequences/{00..10}/{velodyne,labels} and
dataset/sequences/{11..21}/velodyne as extracted after downloading the dataset.
In _mode_ _compute_ all the statistics will first be calculated before being plotted.
Set _save_dir_ to a valid path in order to save the calculated statistics to csv files.
In case you already computed all the data and just want to redo the plots, the script must be called with a path where 
all the generated csv files with the statistics are located and _mode_ must be set to _from_data_.
In both cases, if _save_dir_ is set, the plots are saved as png files to the specified location.

Take a look at the description of the file with `python analyse_total.py --help`.

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

`analyse_total.py` is similarly parametrized as above. Take a look at the help description.

```
Usage: analyse_total.py [OPTIONS] PATH

Options:
  --mode [from_folder|from_files]   If from_folder is selected, PATH must must contain all csv files
                                    of the single sequences. All statistics will be calculated from
                                    the data. If from_files is selected, DIR must be a path to a 
                                    folder where csv files with the combined computed statistics 
                                    are located.
  --save                            If True, save to PATH.
  --help                            Show this message and exit.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## References
[1] J. Behley and M. Garbade and A. Milioto and J. Quenzel and S. Behnke and C. Stachniss and J. Gall, 
"SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences", ICCV 2019

[2] A. Geiger and P. Lenz and C. Stiller and R. Urtasun, Vision meets Robotics: The KITTI Dataset, IJRR 2013
