# Geometric Autoencoder

This repository provides the code for the **ICML 2023** paper [Geometric Autoencoders - What You See is What You Decode](https://proceedings.mlr.press/v202/nazari23a.html).

## Getting Started

Clone the Repository

```
git clone https://github.com/phnazari/GeometricAutoencoder.git
```

Create and activate a new Conda Environment

```
conda create --name my_environment
conda activate my_environment
```

Install `pip`, a package management software for python:

```
conda install pip
```

Change into the project directory and install the dependencies

```
cd GeometricAutoencoder
pip3 install -r requirements.txt
```

Next, you want to add this project to your environment's `PYTHONPATH`. First, find out the projects path by running
```
pwd
```
The output will be something like `/path/to/GeometricAutoencoder`. Second, find out where your virtual environment was installed by running
```
conda info
```
There will be a row titled `active env location`, which will carry a value like `/path/to/my_environment`. Create a file `/path/to/my_environment/lib/pythonX.XX/site-packages/custom.pth`, where `X.XX` is your Python version (which you can find out by running `python3 --version`). In this file, paste
```
/path/to/GeometricAutoencoder
```

You have successfully added the project to the `PYTHONPATH`. Finally, you will have to restart the environment:
```
conda deactivate
conda activate my_environment
```

While TorchVision takes care of the MNIST and FashionMNIST datasets, you will have to [download](http://cb.csail.mit.edu/cb/densvis/datasets/) the PBMC, Zilionis and CElegans datasets yourself.

## Reproducing the Results

### TL; DR
If you want to reproduce our results for MNIST, you can do so by executing

```
bash main.sh
```

### More Detailed

What happens in this case, is that you first train a Geometric Autoencoder by executing
```
bash scripts/create_eval_configs.sh.
```
The training results will be placed in a folder called "save_config", and you will have to move them to the `experiments` folder in order to proceed with the evaluation. The first run, for example, should be moved like

```
mv save_config/1 experiments/train_model/evaluation/repetitions/rep1/MNIST/GeomReg
```

You can then run our geometric diagnostics by envoking
```
python3 exp/analysis.py
```
and the quantitative metrics by executing
```
python3 scripts/load_results.py
```


## The Differential Geometry
The differential geometry can be found inside directory `src/diffgeo`. Our geometric regularizer is implemented in `src/criterions.py`.



## Converting ParametricUMAP (UMAP AE) to a PyTorch Model
In order to run our novel diagnostics on a ParametricUMAP autoencoder, it needs to be converted from a TensorFlow model to a PyTorch model. This can be done via the `convert()` function in the `exp/actions.py` file.


# Bibtex
If you use our work, please cite the following publication:


    @InProceedings{pmlr-v202-nazari23a,
      title = {Geometric Autoencoders - What You See is What You Decode},
      author = {Nazari, Philipp and Damrich, Sebastian and Hamprecht, Fred A},
      booktitle = {Proceedings of the 40th International Conference on Machine Learning},
      year = {2023},
      volume = {202},
      }
