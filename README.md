# 🔍 Survey Quality Detection using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange.svg)](https://scikit-learn.org/)

## 📊 Overview

A comprehensive Python toolkit for detecting fraudulent and low-quality responses in online surveys using multiple detection strategies:
- ✅ Attention check questions
- ✅ Logical contradiction analysis
- ✅ Statistical variance detection
- ✅ Machine Learning classification (Random Forest, SVM, Logistic Regression, XGBoost)

## 🎯 Key Features

- **Automated Quality Assessment**: Identifies clean, suspicious, and fraudulent responses
- **Multi-Strategy Detection**: Combines 4 detection methods for robust fraud detection
- **ML-Powered Classification**: Achieves 100% accuracy using ensemble methods
- **Excel Report Generation**: Creates formatted analysis reports with conditional formatting
- **Bilingual Support**: Arabic and English interface
- **Google Colab Compatible**: Ready-to-use in cloud environments

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `Survey_Analyzer_Colab.py` | Google Colab version with file upload interface |
| `ML_Analysis_With_Figures.py` | Complete ML analysis with 5 publication-ready figures |
| `Complete_Survey_Analyzer_GUI.py` | Desktop GUI version for Windows/Mac/Linux |
| `survey_data_generator.py` | Generate simulated survey data for testing |

## 🚀 Quick Start

### Google Colab (Easiest)

1. Open Google Colab: https://colab.research.google.com
2. Upload `Survey_Analyzer_Colab.py`
3. Run all cells
4. Upload your survey data (CSV or Excel) when prompted
5. Download the generated analysis Excel file

### Local Installation

```bash
# Install dependencies
pip install pandas numpy openpyxl scikit-learn matplotlib seaborn xgboost

# Run the analyzer
python Survey_Analyzer_Colab.py
```

### Desktop GUI Version

```bash
# For Windows/Mac users with tkinter support
python Complete_Survey_Analyzer_GUI.py
```

## 📊 Detection Methods

### 1. Attention Check Questions
Direct instruction questions embedded in the survey:
- Example: "Please select 'Neutral' for this question"
- **Results**: 94.4% success rate (real data) vs 80.0% (simulated data)

### 2. Logical Contradictions
Detects inconsistent response patterns:
- **Emotional contradictions**: High frustration + High happiness
- **Time paradoxes**: "Waste time" + "Full control"
- **Detection rate**: 35.8% in real data, 11.1% in simulated

### 3. Variance Analysis
Statistical detection of straight-lining:
- Individual standard deviation (SD < 0.5 = suspicious)
- **Detection rate**: 2.8% in real data, 5.6% in simulated

### 4. Machine Learning Classification
Four algorithms trained on labeled data:

| Algorithm | Accuracy | Precision | Recall | F1-Score | AUC |
|-----------|----------|-----------|--------|----------|-----|
| **Random Forest** | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| **SVM** | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| **Logistic Regression** | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| **XGBoost** | 0.998 | 0.997 | 0.999 | 0.998 | 1.000 |

## 📈 Feature Importance

Analysis reveals the most effective detection features:

1. **Time Contradiction** (49.2%) - Most important
2. **Q4 Attention Check** (18.9%)
3. **Emotional Contradiction** (14.2%)
4. **Q7 Attention Check** (12.3%)
5. **Standard Deviation** (4.0%)
6. **Low Variance** (1.5%)

## 📦 Requirements

```
pandas >= 1.5.0
numpy >= 1.24.0
openpyxl >= 3.1.0
scikit-learn >= 1.3.0
matplotlib >= 3.7.0
seaborn >= 0.12.0
xgboost >= 2.0.0
```

## 📊 Output Files

The scripts generate:

### Excel File (6 Sheets)
1. **Complete Data** - All responses combined
2. **Real Data** - Original survey responses
3. **Fake Data** - Simulated responses (if provided)
4. **Quality Analysis** - Color-coded classification results
5. **Statistics** - Demographic distributions
6. **User Guide** - Instructions in Arabic/English

### Figures (PNG, 300 DPI)
- `Fig1_Performance.png` - Algorithm comparison
- `Fig2_ConfusionMatrix.png` - Classification matrix
- `Fig3_FeatureImportance.png` - Feature weights
- `Fig4_RadarChart.png` - Multi-metric visualization
- `Fig5_ROC.png` - ROC curves with AUC scores

## 📄 Citation

If you use this code in your research, please cite:

```bibtex
@software{survey_quality_detection_2025,
  author = {[Your Name]},
  title = {Survey Quality Detection using Machine Learning},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/YourUsername/Survey-Quality-Detection}
}
```
## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Developed for academic research on survey data quality
- Tested on 199 responses (109 real + 90 simulated)
- Methodology validated against international standards
---

**⭐ Star this repository if you find it useful!**
