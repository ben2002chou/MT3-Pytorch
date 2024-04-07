## MT3: Multi-Task Multitrack Music Transcription - Pytorch

This is a personal-use fork from https://github.com/kunato/mt3-pytorch with some working updates to run code.

## Usage

Converted pretrained weights can be found at original repo: https://github.com/kunato/mt3-pytorch/blob/master/pretrained/mt3.pth

```python
from inference import InferenceHandler

handler = InferenceHandler('./pretrained')
handler.inference('music.mp3')
```

```bash
python mt3_net.py
```

## Citations

```bibtex
@article{gardner2021mt3,
  title={MT3: Multi-Task Multitrack Music Transcription},
  author={Gardner, Josh and Simon, Ian and Manilow, Ethan and Hawthorne, Curtis and Engel, Jesse},
  journal={arXiv preprint arXiv:2111.03017},
  year={2021}
}
```