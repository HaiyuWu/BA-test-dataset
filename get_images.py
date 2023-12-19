import numpy as np
from os import path, makedirs
from tqdm import tqdm
import cv2
import lzma
import pickle
import argparse


def extract(args):
    with lzma.open(args.zx_file, "rb") as fb:
        imgs, im_names = pickle.load(fb, encoding="bytes")
        for i in tqdm(range(len(imgs))):
            # decode from byte
            img = cv2.imdecode(np.asarray(bytearray(imgs[i])), cv2.IMREAD_COLOR)
            # resize to 112x112
            img = cv2.resize(img, (112, 112))
            save_folder = path.join(args.destination, path.split(im_names[i])[0])
            if not path.exists(save_folder):
                makedirs(save_folder)
            cv2.imwrite(path.join(args.destination, im_names), img)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="BA-test dataset extraction."
    )
    parser.add_argument(
        "--zx_file", "-zx", help="The path of .zx file.", type=str
    )
    parser.add_argument(
        "--destination", "-dest", help="Destination.", type=str, default="./BA-test/images"
    )
