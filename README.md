# Artificial Intelligence in Clinical Data Analysis: A Review of Large Language Models, Foundation Models, Digital Twins, and Allergy Applications

## Overview
This repository contains the implementation code and analysis scripts supporting our review paper on artificial intelligence applications in clinical data analysis. We demonstrate two key explainable AI (XAI) techniques: SHAP (SHapley Additive exPlanations) for tabular data and Grad-CAM (Gradient-weighted Class Activation Mapping) for medical imaging.

## Repository Structure
```
.
├── README.md
├── SHAP_PIMA_DATA.ipynb    # SHAP analysis on diabetes prediction
└── cam.py                   # Grad-CAM implementation for chest X-rays
```

## Code Descriptions

### 1. SHAP Analysis (`SHAP_PIMA_DATA.ipynb`)
- **Purpose**: Demonstrates interpretable machine learning for diabetes prediction
- **Dataset**: Pima Indians Diabetes Database
- **Model**: Random Forest Classifier
- **Key Features**:
  - SHAP value computation for feature importance visualization
  - Visualization export

### 2. Grad-CAM Visualization (`cam.py`)
- **Purpose**: Visual explanation of chest X-ray classification decisions
- **Dataset**: NIH ChestX-ray14 dataset
- **Model**: Pre-trained DenseNet121 from TorchXRayVision
- **Key Features**:
  - Heatmap generation highlighting regions of interest
  - Visualization of original and Grad-CAM overlays

## Installation and Usage

### Prerequisites
```bash
# For SHAP analysis
pip install pandas scikit-learn shap matplotlib

# For Grad-CAM visualization
pip install torch torchvision torchxrayvision pytorch-grad-cam pillow
```

### Running the Code

#### SHAP Analysis
1. Open `SHAP_PIMA_DATA.ipynb` in Jupyter Notebook or JupyterLab
2. Execute cells sequentially
3. Output: ROC curve display and `shap_summary_plot_class1.tiff`

#### Grad-CAM Visualization
```bash
# Using uv package manager (recommended)
uv run cam.py

# Or using standard Python
python cam.py
```
Output: `cam.png` containing the Grad-CAM visualization

## Data Sources and Citations

### Diabetes Dataset (SHAP Analysis)
- **Source**: Pima Indians Diabetes Database
- **Reference**: Smith JW, Everhart JE, Dicksont WC, Knowler WC, Johannes RS. Using the ADAP Learning Algorithm to Forecast the Onset of Diabetes Mellitus. *Proc Annu Symp Comput Appl Med Care* 1988; Nov 9: 261–5.
- **Access**: Available through [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/pima+indians+diabetes)

### Chest X-ray Dataset (Grad-CAM)
- **Source**: NIH Chest X-rays dataset
- **Reference**: Wang X, Peng Y, Lu L, Lu Z, Bagheri M, Summers RM. ChestX-ray8: Hospital-scale chest X-ray database and benchmarks on weakly-supervised classification and localization of common thorax diseases. *Proc IEEE Conf Comput Vis Pattern Recognit* 2017; 2017-Jan: 3462–71.
- **Access**: 
  - [NIH Clinical Center Dataset](https://www.nih.gov/news-events/news-releases/nih-clinical-center-provides-one-largest-publicly-available-chest-x-ray-datasets-scientific-community)
  - [CXR8 Dataset on Box](https://nihcc.app.box.com/v/ChestXray-NIHCC/folder/36938765345)

### Software Libraries
- **SHAP**: Lundberg SM, Lee SI. A unified approach to interpreting model predictions. *Adv Neural Inf Process Syst* 2017; 30: 4766–75.
  - Documentation: [https://shap.readthedocs.io/en/latest/](https://shap.readthedocs.io/en/latest/)
- **TorchXRayVision**: Cohen JP, Viviano JD, Bertin P, Morrison P, Torabian P, Guarrera M, et al. TorchXRayVision: A library of chest X-ray datasets and models. *Proc Mach Learn Res* 2021; 172: 231–49.
- **Grad-CAM**: Selvaraju RR, Cogswell M, Das A, Vedantam R, Parikh D, Batra D. Grad-CAM: Visual Explanations From Deep Networks via Gradient-Based Localization. *Proc IEEE Int Conf Comput Vis* 2017: 618–26.
- **Random Forest**: Breiman L. Random forests. *Mach Learn* 2001; 45(1): 5–32.

## License
This code is released under the MIT License. Please note that the datasets and third-party libraries referenced are subject to their respective licenses. Users are responsible for ensuring compliance with all applicable licenses.

## Contact
For questions or issues regarding this code, please open an issue in this repository or contact the corresponding author.

## Acknowledgments
We thank Dr. Hisahiro Ikari for providing the Grad-CAM implementation code (cam.py).

## Citation
```bibtex
@article{FuseAI2025,
  title={Artificial Intelligence in Clinical Data Analysis: A Review of Large Language Models, Foundation Models, Digital Twins, and Allergy Applications},
  author={[Yutaro Fuse, Shawn N Murphy, Hisahiro Ikari, Akiko Takahashi, Kenshiro Fuse, Eiryo Kawakami]},
  journal={[Allergology International]},
  year={2025},
  volume={},
  pages={},
  doi={}
}
```
