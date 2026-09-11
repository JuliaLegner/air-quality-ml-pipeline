# 🌍 Air Quality Classification Pipeline

An end-to-end Python machine learning project that retrieves real-world air pollution data from the OpenWeatherMap API, processes pollutant measurements, and trains classification models to predict Air Quality Index (AQI) categories.

The project demonstrates REST API integration, automated data collection, data preprocessing, machine learning, model evaluation and automated testing.

## 📌 Project Overview

Air pollution is influenced by several pollutants, including particulate matter, nitrogen dioxide, carbon monoxide and ozone.

This project builds a complete data pipeline that collects air-quality measurements for **60 locations worldwide** using the OpenWeatherMap Air Pollution API.

The collected data is transformed into a structured dataset and used to train and compare two machine learning classifiers:

- Random Forest Classifier
- Gradient Boosting Classifier

The aim is to predict the **Air Quality Index (AQI)** based on measured pollutant concentrations.

## 🔄 Project Workflow

```text
Worldwide Locations
        ↓
OpenWeatherMap API
        ↓
Raw Air Pollution Data
        ↓
Data Cleaning & Processing
        ↓
Feature Normalisation
        ↓
Processed Dataset
        ↓
Machine Learning
        ↓
Random Forest ── Gradient Boosting
        ↓
Model Evaluation & Comparison
        ↓
Results Summary
```

## 📊 Data

The pipeline begins with a dataset containing 60 worldwide locations.

For each location, air-pollution measurements are retrieved through the OpenWeatherMap API.

The features include:

| Feature | Description |
|---|---|
| CO | Carbon monoxide |
| NO | Nitrogen monoxide |
| NO₂ | Nitrogen dioxide |
| O₃ | Ozone |
| SO₂ | Sulphur dioxide |
| PM2.5 | Fine particulate matter |
| PM10 | Particulate matter |
| NH₃ | Ammonia |

The target variable is the **Air Quality Index (AQI)** returned by the API.

## 🧠 Machine Learning Models

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to classify AQI levels based on pollutant concentrations.

### Gradient Boosting Classifier

Gradient Boosting sequentially combines multiple weak learners to create a stronger predictive model.

Both classifiers are trained on the processed air-quality dataset and their classification accuracy is compared to determine the better-performing model.

## 🛠️ Technologies

- Python
- pandas
- NumPy
- scikit-learn
- OpenWeatherMap REST API
- JSON
- python-dotenv
- PyTest
- Git & GitHub

## 📁 Project Structure

```text
air-quality-ml-pipeline/
│
├── data/
│   └── worldwide_locations.csv
│
├── notebooks/
│   ├── api.py
│   ├── dataset.py
│   ├── results.py
│   └── train.py
│
├── .gitignore
├── README.md
├── main.py
├── requirements.txt
└── test.py
```

### File Overview

**`main.py`**  
Runs the complete pipeline from data collection through preprocessing, model training and evaluation.

**`notebooks/api.py`**  
Handles communication with the OpenWeatherMap Air Pollution API and retrieves pollution measurements for specified locations.

**`notebooks/dataset.py`**  
Handles the data pipeline, including loading locations, retrieving pollution data, storing raw responses, combining observations and preprocessing the data for modelling.

**`notebooks/train.py`**  
Trains the Random Forest and Gradient Boosting classifiers and evaluates their performance.

**`notebooks/results.py`**  
Handles model results and saves a summary of classifier performance.

**`test.py`**  
Contains the PyTest test suite covering the major components of the pipeline. API calls are mocked so tests can run without making live API requests.

**`data/worldwide_locations.csv`**  
Contains the worldwide locations used to collect air-quality measurements.

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/JuliaLegner/air-quality-ml-pipeline.git
cd air-quality-ml-pipeline
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## 🔑 API Configuration

The project requires an OpenWeatherMap API key.

Create a `.env` file in the project root and add your API key:

```text
API_KEY=your_key_here
```

The `.env` file should remain excluded from version control through `.gitignore`.

> **Important:** Never commit API keys or other credentials to a public repository.

## ▶️ Running the Project

Run the complete pipeline from the project root:

```bash
python main.py
```

The pipeline will:

1. Load the worldwide locations
2. Retrieve air-pollution data from the API
3. Store and process the API responses
4. Create the modelling dataset
5. Normalise the pollutant features
6. Train the Random Forest classifier
7. Train the Gradient Boosting classifier
8. Compare model performance
9. Save the results

## 🧪 Testing

Run the test suite from the project root:

```bash
pytest test.py -v
```

The tests cover the main components of the data collection, preprocessing and machine-learning pipeline.

External API requests are mocked during testing, allowing the pipeline to be tested without relying on a live API connection.

## 📤 Pipeline Outputs

Running the complete pipeline generates:

### Raw Data

```text
data/raw/
```

Stores the raw API responses collected for each location.

### Processed Data

```text
data/processed/air_pollution_processed.csv
```

Contains the cleaned and normalised air-pollution dataset used for model training.

### Model Results

```text
reports/results_summary.txt
```

Stores classifier accuracy results and identifies the best-performing model.

## 💡 Skills Demonstrated

This project demonstrates practical experience in:

- REST API integration
- Automated data collection
- JSON data processing
- Data cleaning and transformation
- pandas and NumPy
- Feature preprocessing and normalisation
- Supervised machine learning
- Random Forest classification
- Gradient Boosting classification
- Model evaluation and comparison
- Modular Python programming
- Automated testing with PyTest
- Mocking external API calls
- Environment-variable management
- End-to-end ML pipeline development

## 🚀 Future Improvements

Potential extensions to the project include:

- Cross-validation
- Hyperparameter optimisation
- Precision, recall and F1-score evaluation
- Confusion matrix visualisation
- Feature importance analysis
- Historical air-quality modelling
- Model persistence for future predictions
- Interactive air-quality dashboards
- Deployment as a prediction API

---

### About

Developed as part of my **MSc Data Science portfolio**, demonstrating an end-to-end Python workflow from external API data collection to machine learning and model evaluation.
