## How to Generate Grad-CAM Output (This file was kindly provided by Dr. Hisahiro Ikari.)
Run the following command to create `cam.png`:
```
uv run cam.py
```

## Data Sources and References

### Chest X-ray Image

The chest X-ray image used in this figure was obtained from the **NIH Chest X-rays dataset**. For more details, please refer to:

- Wang X, Peng Y, Lu L, Lu Z, Bagheri M, Summers RM. *ChestX-ray8: Hospital-scale chest X-ray database and benchmarks on weakly-supervised classification and localization of common thorax diseases.* Proc IEEE Conf Comput Vis Pattern Recognit 2017; 2017-Jan: 3462–71.
- NIH Clinical Center provides one of the largest publicly available chest X-ray datasets to the scientific community. [Available here](https://www.nih.gov/news-events/news-releases/nih-clinical-center-provides-one-largest-publicly-available-chest-x-ray-datasets-scientific-community) [accessed April 23, 2025].
- [CXR8 Dataset on Box](https://nihcc.app.box.com/v/ChestXray-NIHCC/folder/36938765345) [accessed April 23, 2025].

### Grad-CAM Implementation

Grad-CAM was developed and analyzed using the **TorchXRayVision** library:

- Cohen JP, Viviano JD, Bertin P, Morrison P, Torabian P, Guarrera M, et al. *TorchXRayVision: A library of chest X-ray datasets and models.* Proc Mach Learn Res 2021; 172: 231–49.

### SHAP Analysis

The SHAP analysis was conducted using the **Pima Indians Diabetes Database**:

- Smith JW, Everhart JE, Dicksont WC, Knowler WC, Johannes RS. *Using the ADAP Learning Algorithm to Forecast the Onset of Diabetes Mellitus.* Proc Annu Symp Comput Appl Med Care 1988; Nov 9: 261–265.
- [SHAP Documentation](https://shap.readthedocs.io/en/latest/) [accessed April 23, 2025].

## License
This code is released under the MIT License. See the [LICENSE](./LICENSE) file for details.

Please note that the datasets and third-party libraries referenced in the [Data Sources and References](#data-sources-and-references) section are subject to their respective licenses. Users are responsible for ensuring compliance with the applicable licenses when using these resources.
