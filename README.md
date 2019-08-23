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
* [Citation](#citation)
* [References](#references)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

I usually like to create a virtual environment for my projects as explained below. However, it is not needed, so you
 can just skip this part and jump to the package installation.

To set up a virtual environment and install the required packages run


```
$ virtualenv --no-site-packages -p python3 ~/path/to/virtualenv
$ source ~/path/to/virtualenv/bin/activate
(virtualenv) $ pip install requirements.txt
```

To exit the virtual environment run
```
(virtualenv) $ deactivate
```


### Installing

Simply clone the repo and you're good to go

```
$ git clone https://github.com/ltriess/semantic_kitti_stats.git
```


### Get the Data

Downoad the data and unzip it in the same folder.
* for the labels: [Semantic KITTI](http://semantic-kitti.org/dataset.html#download)
* for the point clouds: [KITTI Odometry](http://www.cvlibs.net/datasets/kitti/eval_odometry.php)

## Running the code

There are two different scripts: `analyse_total.py` can only be run when the data was previously generated with 
`analyse_sequence.py`. The latter one gives analysis only for a specific sequence of the dataset. A total evaluation 
based on the computed per sequence statistics can be generated with the first script.

`analyse_sequence.py` can be called with a path to a specific sequence, e.g. _/path/to/dataset/sequences/03_ if _mode_ 
is selected as _from_sequence_. In this case all the statistics will first be calculated before being plotted. Set 
_save_dir_ to a valid path in order to save the calculated statistics to csv files.
In case you already computed all the data and just want to redo the plots, the script must be called with a path where 
all the generated csv files with the statistics are located and _mode_ must be set to _from_data_.
In both cases, if _save_dir_ is set, the plots are saved as png files to the specified location.

Take a look at the description of the file with `python analyse_total.py --help`.

```
Usage: analyse_sequence.py [OPTIONS] PATH

Options:
  --mode [from_sequence|from_data]  If from_sequence is selected, PATH must be a path to a sequence. 
                                    All statistics will be calculated from the data. If from_data is
                                    selected, DIR must be a path to a folder where csv files with the
                                    computed statistics are located.
  --save_dir PATH                   Path where to save the generated graphs. If not provided, show on display.
  --help                            Show this message and exit.
```

`analyse_total.py` is similarly parametrized as above. Take a look at the help description.

```
Usage: analyse_total.py [OPTIONS] PATH

Options:
  --mode [from_folder|from_files]   If from_folder is selected, DIR must be a path to the csv file 
                                    of the singles equences. All statistics will be calculated from 
                                    the data. If from_files is selected, DIR must be a path to a 
                                    folder where csv files with the combined computed statistics 
                                    are located.
  --save                            If True, save to PATH.
  --help                            Show this message and exit.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Citation

If you use this code in your work, please cite as
```
@misc{Triess2019,
  author = {Larissa Triess},
  title = {Dataset Statistics for Semantic KITTI},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ltriess/semantic_kitti_stats}}
}
```

## References
[1] J. Behley and M. Garbade and A. Milioto and J. Quenzel and S. Behnke and C. Stachniss and J. Gall, 
"SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences", ICCV 2019

[2] A. Geiger and P. Lenz and C. Stiller and R. Urtasun, Vision meets Robotics: The KITTI Dataset, IJRR 2013
