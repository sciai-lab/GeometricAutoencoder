import os
import torch

os.environ["GEOMSTATS_BACKEND"] = "pytorch"

from evaluation import evaluate

model_paths = []

datasets = [
    "MNIST",
    # "Earth",
    "FashionMNIST",
    "CElegans",
    "Zilionis_normalized",
    "PBMC_new"
]

models = [
    # "Vanilla",
    # "TopoReg",
    # "GeomReg",
    # "PCA",
    # "TSNE",
    # "UMAP",
    "ParametricUMAP"
]

diagnostics = [
    "indicatrices",
    "determinants",
    "embedding"
]

base = os.path.join(os.path.dirname(__file__), '..', "experiments")

for dataset in datasets:
    for model in models:
        if model in ["Vanilla", "TopoReg", "GeomReg"]:
            dir = "train_model"
        else:
            dir = "fit_competitor"

        model_paths.append(os.path.join(base, dir, "evaluation/repetitions/rep1", dataset, model, "model_state.pth"))

# model_paths = [os.path.join("/export/home/pnazari/workspace/AutoEncoderVisualization/save_config/MNIST/ParametricUMAP",
#                            "model_state.pth")]

for i, model_path in enumerate(model_paths):
    img_path = model_path.split("/")[-2]
    dataset = model_path.split("/")[-3]
    model_name = model_path.split("/")[-2]

    evaluate(writer_dir="test",
             model_path=model_path,
             img_path=img_path,
             dataset_name=dataset,
             model_name=model_name,
             used_diagnostics=diagnostics)
