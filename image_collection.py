import shutil
import pandas as pd
import numpy as np
from os import path, makedirs
import argparse


def im_name_collection(csv_label_file):
    return np.array(pd.read_csv(csv_label_file))[:, 0]


def im_path_grouping(im_path_file):
    im_path_dict = {}
    im_paths = np.genfromtxt(im_path_file, str)
    for im_path in im_paths:
        sep = im_path.split("/")
        im_path_dict[f"{sep[-2]}/{sep[-1]}"] = im_path
    return im_path_dict


def dataset_collection(csv_label_file,
                       im_path_file,
                       destination):
    image_names = im_name_collection(csv_label_file)
    path_dict = im_path_grouping(im_path_file)
    for image_name in image_names:
        aim_folder = path.join(destination, image_name.split("/")[0])
        if not path.exists(aim_folder):
            makedirs(aim_folder)
        shutil.copy(path_dict[image_name], aim_folder)
    print("Done!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Ba-test dataset collection."
    )
    parser.add_argument(
        "--im_path_file", "-im_path", help="The file stores image paths.", type=str
    )
    parser.add_argument(
        "--label_file", "-label", help="Dataset label file.", type=str
    )
    parser.add_argument(
        "--destination", "-dest", help="Destination.", type=str, default="./BA-test/images"
    )
    args = parser.parse_args()

    dataset_collection(args.label_file,
                       args.im_path_file,
                       args.destination)
