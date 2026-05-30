# RecA-QSAR-FDA-Bayesian-Docking

Publication-ready computational workflow for the discovery of novel Mycobacterium tuberculosis RecA inhibitors using machine learning, QSAR modeling, Bayesian fingerprint analysis, FDA-approved drug repurposing, and molecular docking.

## Project Overview

This repository presents an end-to-end cheminformatics workflow for identifying potential RecA inhibitors targeting Mycobacterium tuberculosis.

The workflow integrates:

- ChEMBL bioactivity data collection and curation
- PaDEL fingerprint generation
- Feature selection using ANOVA F-score and RFE benchmarking
- Classical machine learning model development
- Model validation and Y-randomization analysis
- Bayesian fingerprint classification
- FDA-approved drug repurposing screening
- Molecular docking validation

## Workflow

1. Data Collection and Curation
2. Molecular Fingerprint Generation
3. Feature Selection
4. Machine Learning Modeling
5. Model Validation
6. Bayesian Classification Analysis
7. FDA Drug Screening
8. Molecular Docking Evaluation

## Repository Structure

```text
1_Data_collection_RecA.ipynb
2_RecA_PaDEL_Fingerprint_Modeling_Matrix.ipynb
3_RecA_Feature_Selection_RFE_Benchmark.ipynb
4_RecA_Classical_ML_Modeling.ipynb
5_6_7_RecA_CONCISE_QSAR_FDA_Bayesian_Docking.ipynb
```

## Dataset

Target:
- Mycobacterium tuberculosis RecA protein

Source:
- ChEMBL Database

Bioactivity Endpoint:
- EC50 (nM)

## Machine Learning Methods

- Random Forest
- Extra Trees
- XGBoost
- Support Vector Machine (RBF)

## Validation Methods

- Cross Validation
- Holdout Test Set
- ROC-AUC Analysis
- Y-Randomization Test
- Bayesian Fingerprint Classification

## Applications

- Tuberculosis drug discovery
- Drug repurposing
- QSAR modeling
- Computational medicinal chemistry
- Machine learning for drug design

## Author

Muhammad Akbar S. Kurniawan

Quantum-Medicinal-Laboratory (Q-MEDLAB)

## License

MIT License
