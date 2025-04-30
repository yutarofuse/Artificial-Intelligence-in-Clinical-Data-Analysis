run this code to create cam.png
```
uv run cam.py
```

The chest X-ray image used in this figure was obtained from the NIH Chest X-rays dataset. For more details, please refer to the following:
	•	Wang X, Peng Y, Lu L, Lu Z, Bagheri M, Summers RM. ChestX-ray8: Hospital-scale chest X-ray database and benchmarks on weakly-supervised classification and localization of common thorax diseases. Proc IEEE Conf Comput Vis Pattern Recognit 2017; 2017-Jan: 3462–71.
	•	NIH Clinical Center provides one of the largest publicly available chest X-ray datasets to the scientific community. Available from: https://www.nih.gov/news-events/news-releases/nih-clinical-center-provides-one-largest-publicly-available-chest-x-ray-datasets-scientific-community [accessed April 23, 2025].
	•	CXR8 | Powered by Box. Available from: https://nihcc.app.box.com/v/ChestXray-NIHCC/folder/36938765345 [accessed April 23, 2025].

Grad-CAM was developed and analyzed using the TorchXRayVision library.
	•	Cohen JP, Viviano JD, Bertin P, Morrison P, Torabian P, Guarrera M, et al. TorchXRayVision: A library of chest X-ray datasets and models. Proc Mach Learn Res 2021; 172: 231–49.

For the SHAP analysis, we used the Pima Indians Diabetes Database. Please refer to the following for details:
	•	Smith JW, Everhart JE, Dicksont WC, Knowler WC, Johannes RS. Using the ADAP Learning Algorithm to Forecast the Onset of Diabetes Mellitus. Proc Annu Symp Comput Appl Med Care 1988; Nov 9: 261–265.
	•	SHAP official documentation: https://shap.readthedocs.io/en/latest/ [accessed April 23, 2025].
