## 新潟大学大学院医歯学総合研究科　顎顔面放射線学分野　大学院演習用
ローカル環境での実行を前提とした版<br>
By. H.Nishiyama

## Windowsにてpipenvを利用する環境
CPU単体（GPU無し）：https://www5.dent.niigata-u.ac.jp/~nisiyama/grad/python/pipenv-sys-install-nonGPU-j.pdf<br>
※Python:3.9.7, TensorFlow:2.17.0<br>
CPU単体での動作用のPipfileについては、<a href="https://github.com/aujinen/AI-yodosha/blob/main/Pipfile_only_CPU.txt">Pipfile_only_CPU.txt<a>内部を参照、ないしコピーして使ってください。<br>
GPU有り：https://www5.dent.niigata-u.ac.jp/~nisiyama/grad/python/pipenv-sys-install-GPU-j.pdf<br>
※CUDA:11.7, cuDNN:8.6.7, Python:3.9.7, TensorFlow-GPU:2.6.0<br>
GPU動作用のPipfileについては、<a href="https://github.com/aujinen/AI-yodosha/blob/main/Pipfile_with_GPU.txt">Pipfile_with_GPU.txt<a>内部を参照、ないしコピーして使ってください。<br>

### 共通ライブラリ
jupyter<br>
matplotlib<br>
japanize-matplotlib<br>
pandas<br>
scikit-learn<br>

## WindowsにてWSL2でのGPUを利用する環境
ubuntu:22.04<br>
Python:3.9.13<br>
cuda:11.8/12.1 (切替)<br>
cudnn:8.6<br>
Tensorflow:2.13<br>
PyTorch:2.4.0<br>

# === 以下、参考資料 ===
## Windowsにてminicondaを利用する環境
https://www5.dent.niigata-u.ac.jp/~nisiyama/grad/python/install-miniconda.pdf

## WindowsにてPytorchを利用する環境
https://www5.dent.niigata-u.ac.jp/~nisiyama/grad/Pipenv-PyTorch.pdf
