# Plant Disease Detection: Multi-Architecture Neural Network Comparison

## Project Overview
This repository contains a comprehensive deep learning pipeline for plant leaf disease classification. The project systematically compares the performance of 8 distinct neural network architectures on a unified 16-class merged dataset (comprising data from PlantDoc and web-sourced images). 

The primary objective is to evaluate how different architectural paradigms ranging from traditional flattened Multi-Layer Perceptrons (MLPs) to state-of-the-art Deep Convolutional Neural Networks (CNNs) handle complex spatial hierarchies and noise in agricultural image data.

## Architectures Implemented
The project fulfills a rigorous evaluation of 4 custom multi-layer networks and 4 pre-trained deep learning architectures:

## 🗄️ Dataset Sources
To fully replicate this project, you must download the raw images and place them in your local `data/` directory before running the merging scripts. Due to GitHub's file size limits, datasets are strictly `.gitignore`d.

The 16-class merged dataset is constructed from two primary sources:
1. **PlantDoc Dataset:** [https://github.com/pratikkayal/PlantDoc-Dataset.git] - A comprehensive, non-laboratory dataset for visual plant disease detection containing images of leaves with various diseases in real-world noise conditions.
2. **Web Sourced Dataset for Plant Disease Detection:** [https://zenodo.org/records/14051480] - Additional images scraped to balance class frequencies and improve the model's generalization capabilities.

### Custom Architectures (Built from Scratch)
1. **MLP Shallow:** A baseline 3-layer dense network to establish classical mathematical mapping performance.
2. **MLP Regularized:** A deeper dense network utilizing 40% Dropout to test stochastic regularization on flattened 1D spatial data.
3. **CNN Baseline:** A custom 3-block convolutional network demonstrating the impact of 2D spatial feature extraction.
4. **CNN Advanced:** A highly optimized 4-block CNN incorporating Batch Normalization to combat internal covariate shift and accelerate learning.

### Deep Learning Architectures (Transfer Learning)
5. **EfficientNet-B0:** A lightweight, highly scaled CNN optimized for parameter efficiency.
6. **EfficientNet-B3:** A deeper variant of EfficientNet for enhanced feature extraction.
7. **ResNet-50:** A 50-layer deep network utilizing residual connections to solve the vanishing gradient problem.
8. **DenseNet-201:** A densely connected network where each layer receives feature maps from all preceding layers, maximizing feature reuse.

## Repository Structure

```text
├── data/                       # (Git-ignored) Directory for raw and processed datasets
├── neural-networks/            # Custom architecture implementations
│   ├── CNN_Advanced.ipynb
│   ├── CNN_Baseline.ipynb
│   ├── MLP_Regularized.ipynb
│   └── MLP_Shallow.ipynb
├── pre-trained-models/         # Transfer learning implementations
│   ├── Densenet201.ipynb
│   ├── EfficientnetB0.ipynb
│   ├── EfficientnetB3.ipynb
│   └── Resnet50.ipynb
├── preprocessing/              # Data exploration and augmentation notebooks
│   └── EDA and Noise.ipynb
├── scripts/                    # Python utility scripts for data engineering
│   ├── merge_datasets.py
│   ├── merge_datasets_true.py
│   ├── rename_images.py
│   └── report_generation.py
├── visualizations/             # Output metrics, confusion matrices, and ROC curves
├── .gitignore
└── requirements.txt            # Python environment dependencies
```

# Evaluation Metrics

Every model in this repository is evaluated using a standardized testing pipeline. Results and visual artifacts are automatically saved to the `visualizations/` directory and include:

- **Confusion Matrices**: Visual heatmaps to track misclassifications across the 16 specific disease classes.
- **Multi-Class ROC-AUC Curves**: One-vs Rest (OvR) plots detailing the trade-off between True Positive and False Positive rates.
- **Classification Reports**: Tabular breakdowns of Precision, Recall, and F1 Scores.

---

## Getting Started

### 1. Environment Setup

Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/yourusername/plant-disease-detection.git
cd plant-disease-detection
pip install -r requirements.txt
```

## 2. Data Preparation

Ensure your raw datasets are placed in the `data/` directory. Run the merging scripts to compile the 16-class datasets and resolve naming collisions.

```bash
python scripts/rename_images.py
python scripts/merge_datasets.py
```
---

## 3. Model Training

Models are trained via their respective Jupyter Notebooks. The custom DataLoader dynamically adjusts image resolution (e.g., downsizing to `64x64` for MLPs to manage VRAM, and maintaining `224x224` for CNNs).

- Navigate to `neural-networks/` or `pre-trained-models/` and execute the notebooks sequentially.
- All notebooks feature built-in early stopping mechanisms based on validation loss monitoring.

---

## Key Findings

- **Spatial Invariance**: Traditional MLPs struggled significantly with the dataset due to the destruction of 2D spatial context during flattening, highlighting the absolute necessity of convolutional layers for image data.

- **Transfer Learning Impact**: Models initialized with ImageNet weights (ResNet, EfficientNet) vastly outperformed models initialized randomly, proving the efficacy of pre-trained feature extractors in domain-specific tasks with limited data.

## References & Acknowledgments
This repository and its comparative methodology were built to implement, evaluate, and expand upon the deep learning architectures proposed in the following research paper:

* **Title:** [Plant Leaf Disease Detection Using Deep Learning: A Multi-Dataset Approach]
* **Authors:** [Manjunatha Shettigere Krishna, Pedro Machado, Richard I. Otuka, Salisu W. Yahaya, Filipe Neves dos Santos and Isibor Kennedy Ihianle]
* **Link:** [https://www.mdpi.com/2571-8800/8/1/4]

The architectural choices, specific 16-class mapping, and evaluation metrics (Confusion Matrix, Multi-Class ROC) directly follow the constraints and objectives outlined in this research.