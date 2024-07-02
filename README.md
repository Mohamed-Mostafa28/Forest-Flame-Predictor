# 🌲🔥 Forest Flame Predictor 🔥🌲

Forest Flame Predictor is a machine learning project designed to predict forest fires in Algeria using the Algerian Forest Fire dataset. This project leverages DVC for data version control and GitHub Actions for continuous integration and deployment.

## 📜 Project Description

This project aims to develop a predictive model for forest fires using the Algerian Forest Fire dataset. The dataset contains meteorological data and fire occurrences from two regions in Algeria.

## 📊 Dataset

The dataset, provided by the UCI Machine Learning Repository, includes various meteorological features and fire occurrences. It is located in the `data/source/Algerian_forest_fires_dataset_UPDATE.csv` file.
URL: https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset

## 🗂 Project Structure
```
Forest-Flame-Predictor/
├── .github/
│ └── workflows/
│ └── CI.yaml
├── data/
│ ├── source/
│ └── processed/
├── output/
│ ├── models/
│ ├── info/
│ └── images/
├── Notebooks/
│ └── EDA.ipynb
├── algerianForestFires/
│ ├── src/
│ │ ├── preprocessing.py
│ │ └── training.py
│ └── utiles/
│ └── Utilities.py
├── .dvc
├── .dvcignore
├── .gitignore
├── dvc.lock
├── dvc.yaml
├── params.yml
├── setup.py
├── template.py
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- [DVC](https://dvc.org/doc/install) (Data Version Control)
- Git

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Mohamed-Mostafa28/Forest-Flame-Predictor.git
    cd Forest-Flame-Predictor
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install DVC:**

    ```bash
    pip install dvc
    ```

5. **Pull the DVC-tracked data:**

    ```bash
    dvc pull
    ```

## 🛠 Usage

1. **Preprocess the data:**

    ```bash
    dvc repro run_prepare
    ```

2. **Train the model:**

    ```bash
    dvc repro run_training
    ```

3. **Evaluate the model:**

    ```bash
    dvc repro run_evaluate
    ```

## 🔄 Continuous Integration

The project uses GitHub Actions for CI/CD. The workflow file is located in `.github/workflows/ci.yml`.

## 🤝 Contribution Guidelines

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. **Open a pull request.**

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- UCI Machine Learning Repository for the Algerian Forest Fire dataset.
- The DVC team for their amazing tool.
- The open-source community for their continuous contributions.

## 📬 Contact

For any questions or suggestions, feel free to open an issue or contact me.





