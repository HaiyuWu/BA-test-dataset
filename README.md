# What Should be Balanced in a "Balanced'' Dataset?
### Paper details

[Haiyu Wu](https://haiyuwu.netlify.app/), [Kevin W. Bowyer](https://www3.nd.edu/~kwb/), *What Should Be Balanced in a "Balanced“ Face Recognition Dataset?*, BMVC, 2023, [arXiv:2304.09818](https://arxiv.org/abs/2304.09818).

### Abstract
> The issue of demographic disparities in face recognition accuracy has attracted increasing attention in recent years. Various face image datasets have been proposed as ’fair’ or ’balanced’ to assess the accuracy of face recognition algorithms across demographics. These datasets typically balance the number of identities and images across
> demographics. It is important to note that the number of identities and images in an evaluation dataset are *not* driving factors for 1-to-1 face matching accuracy. Moreover, balancing the number of identities and images does not ensure balance in other factors known to impact accuracy, such as head pose, brightness, and image quality. We demonstrate these issues using several recently proposed datasets. To improve the ability to perform less biased evaluations, we propose a bias-aware toolkit that facilitates creation of cross-demographic evaluation datasets balanced on factors mentioned in this paper.

### Citation
If you use any part of our code or dataset, please cite our paper and VGGFace2 paper.
```
@article{wu2023real,
  title={A Real Balanced Dataset For Understanding Bias? Factors That Impact Accuracy, Not Numbers of Identities and Images},
  author={Wu, Haiyu and Bowyer, Kevin W},
  journal={arXiv preprint arXiv:2304.09818},
  year={2023}
}

@inproceedings{cao2018vggface2,
  title={Vggface2: A dataset for recognising faces across pose and age},
  author={Cao, Qiong and Shen, Li and Xie, Weidi and Parkhi, Omkar M and Zisserman, Andrew},
  booktitle={2018 13th IEEE international conference on automatic face \& gesture recognition (FG 2018)},
  pages={67--74},
  year={2018},
  organization={IEEE}
}
```
### Dataset Collection

You need to have the VGGFace2 (original version) dataset first, then use [file_path_extractor.py](https://github.com/HaiyuWu/LogicalConsistency/blob/main/file_path_extractor.py) to collect the image paths:

```
python3 file_path_extractor.py -s folder/path/of/vggface2 -d ./ -sfn vggface2 -end_with jpg
```

Then collecting BA-test images by running [image_collection.py](https://github.com/HaiyuWu/BA-test-dataset/blob/main/image_collection.py) to collect the images and store the image paths to the "BA-test.txt" file.

```
python3 image_collection.py -im_path vggface2.txt -label ./BA-test/labels.csv
```

The last step is using [run_face_alignment.py](https://github.com/vitoralbiero/img2pose#align-faces) in [img2pose repo](https://github.com/vitoralbiero/img2pose) to crop and align images.

### Benchmark Collection

After you having the BA-test dataset, you can simply run [image_collection.py](https://github.com/HaiyuWu/BA-test-dataset/blob/main/image_collection.py) to collect the benchmark images.
```
python3 image_collection.py -im_path BA-test.txt -label ./benchmark/benchmark_labels.csv -dest ./benchmark/images -n BA-test_benchmark
```
