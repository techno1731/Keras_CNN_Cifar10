# CNN on Cifar10 with Keras

This repo contains all the modules required to launch a Heroku App like this one:

https://cnn-cifar10-bts.herokuapp.com/

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
