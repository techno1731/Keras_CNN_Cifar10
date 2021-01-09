# CNN on Cifar10 with Keras

**Powered by:**

[![Python](https://img.shields.io/pypi/pyversions/tensorflow?logo=python&logoColor=white)]
[![Tensorflow](https://img.shields.io/badge/Tensorflow-CPU-2.3.2-orange?logo=tensorflow)](https://github.com/tensorflow/tensorflow)
[![Keras](https://img.shields.io/badge/keras-2.4-red?logo=keras)](https://github.com/keras-team/keras)
[![Numpy](https://img.shields.io/badge/Numpy-1.19.5-skyblue?logo=numpy)](https://github.com/numpy/numpy)
[![Streamlit](https://img.shields.io/badge/streamlit-0.74.1-yellow)](https://github.com/streamlit/streamlit)
[![Heroku](https://img.shields.io/badge/Heroku-7.47.7-purple?logo=Heroku)](https://github.com/heroku/cli)
[![Black](https://img.shields.io/badge/Code%20Style-Black-black)](https://github.com/psf/black)

## What is it?

This repo contains all the modules required to launch a Heroku App that classifies images into the ten categories from CIFAR10 dataset, the model was trained with convolutional neural networks using keras sequential wrapper on tensorflow.

Demo site: https://cnn-cifar10-bts.herokuapp.com/

Model training notebook is not included. But h5 file with the trained model is. 

## Installation

If you want to use it as the base for your own project you can do it by following the below instructions.

Requirements:

- Git
- Heroku
- Python 3.8.X or higher with pip3 installed
- See requirements.in for dependencies

Clone the repository into any directory you want by doing:

```bash
git clone https://github.com/techno1731/Keras_CNN_Cifar10.git
```
then cd into the Keras_CNN_Cifar10 folder and remove all git files. Linux example below:

In Linux or any UNIX like bash shell:

```bash
rm -rf .git*
```
Change into your virtual environment or create one for this project with your favorite tool, pyenv, venv, virtualenv, etc.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pip-tools.

```bash
pip install pip-tools
```
Then install the requirements into your virtual environment (recommended) by doing:

```bash
pip-sync
```
That's it you have an environment ready to develop with the codebase.

## Usage

A demo of the application is available online at:

https://cnn-cifar10-bts.herokuapp.com/

To run the application locally after following installation instructions do:

```bash
streamlit run streamlit_deployment.py
```
The simply upload a picture and the app will return some strings with the result.

## License
[MIT](https://choosealicense.com/licenses/mit/)
