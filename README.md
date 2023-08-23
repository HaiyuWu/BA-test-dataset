# What Should be Balanced in a "Balanced'' Dataset?
### Paper details

[Haiyu Wu](https://haiyuwu.netlify.app/), [Kevin W. Bowyer](https://www3.nd.edu/~kwb/), *What Should Be Balanced in a "Balanced“ Face Recognition Dataset?*, BMVC, 2023, [arXiv:2304.09818](https://arxiv.org/abs/2304.09818).

### Abstract
> The issue of demographic disparities in face recognition accuracy has attracted increasing attention in recent years. Various face image datasets have been proposed as ’fair’ or ’balanced’ to assess the accuracy of face recognition algorithms across demographics. These datasets typically balance the number of identities and images across
> demographics. It is important to note that the number of identities and images in an evaluation dataset are *not* driving factors for 1-to-1 face matching accuracy. Moreover, balancing the number of identities and images does not ensure balance in other factors known to impact accuracy, such as head pose, brightness, and image quality. We demonstrate these issues using several recently proposed datasets. To improve the ability to perform less biased evaluations, we propose a bias-aware toolkit that facilitates creation of cross-demographic evaluation datasets balanced on factors mentioned in this paper.

### Citation
If you use any part of our code or data, please cite our paper.
```
@article{wu2023real,
  title={A Real Balanced Dataset For Understanding Bias? Factors That Impact Accuracy, Not Numbers of Identities and Images},
  author={Wu, Haiyu and Bowyer, Kevin W},
  journal={arXiv preprint arXiv:2304.09818},
  year={2023}
}
```
### Dataset Collection

You need to have the VGGFace2 (original version) dataset first, then use [file_path_extractor.py](https://github.com/HaiyuWu/LogicalConsistency/blob/main/file_path_extractor.py) to collect the image paths:

```
python file_path_extractor.py -s folder/path/of/vggface2 -d ./ -sfn vggface2 -end_with jpg
```


### Benchmark Collection
