# 📊 Project Findings — Air Quality Classification Pipeline

## 🌍 Overview

This project developed an end-to-end machine learning pipeline for collecting, processing and modelling real-world air pollution data.

Air-quality measurements were retrieved for **60 worldwide locations** using the OpenWeatherMap Air Pollution API.

The project demonstrates the complete workflow from:

```text
External API
     ↓
Raw Data Collection
     ↓
Data Processing
     ↓
Feature Normalisation
     ↓
Machine Learning
     ↓
Model Evaluation
     ↓
Automated Testing
```

Two supervised machine-learning algorithms were implemented and compared:

- 🌲 Random Forest Classifier
- 🚀 Gradient Boosting Classifier

The objective was to predict **Air Quality Index (AQI) categories** using measured pollutant concentrations.

---

# 🌫️ Finding 1 — Air Quality Can Be Represented Through Multiple Pollutants

The modelling dataset contains eight pollutant measurements:

| Pollutant | Description |
|---|---|
| CO | Carbon monoxide |
| NO | Nitrogen monoxide |
| NO₂ | Nitrogen dioxide |
| O₃ | Ozone |
| SO₂ | Sulphur dioxide |
| PM2.5 | Fine particulate matter |
| PM10 | Particulate matter |
| NH₃ | Ammonia |

Rather than relying on a single environmental measurement, the model uses these pollutant concentrations together to predict AQI.

### 💡 Key Takeaway

Air-quality classification is a **multivariable problem**.

The machine-learning models can evaluate several pollutant measurements simultaneously rather than relying on manually defined rules for individual variables.

---

# 🌐 Finding 2 — APIs Enable Automated Real-World Data Collection

One of the main technical outcomes of the project was the integration of the **OpenWeatherMap Air Pollution API**.

The pipeline automatically:

```text
Loads Location
      ↓
Sends API Request
      ↓
Receives JSON Response
      ↓
Extracts Pollution Measurements
      ↓
Stores Observation
      ↓
Moves to Next Location
```

This process is repeated across the worldwide locations included in the dataset.

### 💡 Key Takeaway

Using an API removes the need to manually collect environmental observations.

The same pipeline structure could be extended to:

- additional locations
- repeated data collection
- historical observations
- scheduled monitoring
- larger environmental datasets

This makes the project more than a static machine-learning notebook: it demonstrates how a model can be connected to an **external data source**.

---

# 🧹 Finding 3 — Raw API Data Must Be Transformed Before Modelling

The API returns structured JSON data that cannot simply be passed directly into the classifiers.

The pipeline therefore separates:

```text
Raw API Response
        ↓
Relevant Variables Extracted
        ↓
Structured Dataset
        ↓
Data Processing
        ↓
Feature Normalisation
        ↓
ML-Ready Dataset
```

Raw API responses are retained separately from the processed modelling data.

### 💡 Key Takeaway

This demonstrates an important machine-learning principle:

> **Model training is only one part of an ML system.**

Data collection, transformation and preprocessing are necessary before modelling can begin.

---

# ⚙️ Finding 4 — Feature Normalisation Creates a Consistent Modelling Input

Pollutant concentrations can exist on substantially different numerical scales.

The project therefore normalises the pollutant features before they are passed through the modelling pipeline.

### 💡 Why This Matters

Without preprocessing, one feature may contain numerically much larger values than another.

Normalisation transforms the features into a more consistent representation for downstream analysis.

The workflow therefore separates:

```text
Raw Pollutant Measurements
          ↓
     Preprocessing
          ↓
Normalised Features
          ↓
 Machine Learning
```

---

# 🧠 Finding 5 — Multiple Models Allow Performance Comparison

Two classification algorithms were implemented.

## 🌲 Random Forest

Random Forest combines multiple decision trees into an ensemble classifier.

The model learns relationships between pollutant concentrations and AQI categories across many individual trees.

## 🚀 Gradient Boosting

Gradient Boosting builds a sequence of weak learners, with later learners attempting to improve errors made earlier in the sequence.

### 💡 Key Takeaway

Implementing multiple classifiers makes it possible to compare alternative modelling approaches rather than assuming that one algorithm will automatically perform best.

The pipeline therefore follows:

```text
Processed Dataset
       │
       ├───────────────┐
       ▼               ▼
 Random Forest   Gradient Boosting
       │               │
       └───────┬───────┘
               ▼
      Performance Comparison
```

---

# 📈 Finding 6 — Model Evaluation Should Determine Model Selection

The pipeline evaluates both classifiers and records their resulting performance.

### Model Comparison

| Model | Accuracy |
|---|---:|
| 🌲 Random Forest | **Add result here** |
| 🚀 Gradient Boosting | **Add result here** |

### 🏆 Best Performing Model

```text
Add result from reports/results_summary.txt
```

### 💡 Interpretation

The preferred model should be selected based on measured performance rather than algorithm reputation or complexity.

Once the final results are added, this section can document:

```text
Model A Accuracy
        vs
Model B Accuracy
        ↓
Performance Comparison
        ↓
Selected Model
```

> The exact model results should be taken directly from the generated `reports/results_summary.txt` file rather than entered manually from memory.

---

# 🧪 Finding 7 — Automated Testing Improves Pipeline Reliability

A particularly important technical component of the project is the use of **PyTest**.

The test suite checks major components of the pipeline.

External API requests are mocked during testing.

This means the tests can verify the program's behaviour without repeatedly making real network requests.

### 💡 Why Mocking Matters

Without mocking:

```text
Test
 ↓
Live API Request
 ↓
Internet/API Dependency
 ↓
Potential Test Failure
```

With mocking:

```text
Test
 ↓
Mock API Response
 ↓
Controlled Input
 ↓
Repeatable Test
```

This makes testing:

- faster
- more predictable
- independent of API availability
- less dependent on API usage limits

### 💡 Key Takeaway

The project demonstrates not only how to build a data pipeline, but also how to **test external dependencies in a controlled way**.

---

# 🔐 Finding 8 — Credentials Should Be Separated From Source Code

The OpenWeatherMap API key is stored through an environment variable rather than being hard-coded into the Python files.

```text
.env
 │
 ▼
API_KEY
 │
 ▼
Python Application
```

The `.env` file is excluded from Git version control.

### 💡 Key Takeaway

Separating credentials from source code is important when publishing projects to GitHub.

It allows the codebase to remain public without exposing private API credentials.

---

# 🧩 Finding 9 — Modular Code Makes the Pipeline Easier to Maintain

The project separates responsibilities across multiple Python modules.

```text
api.py
│
├── API communication
│
dataset.py
│
├── Data collection
├── Data processing
└── Dataset preparation
│
train.py
│
├── Model training
└── Model evaluation
│
results.py
│
└── Result handling
│
main.py
│
└── Pipeline orchestration
```

### 💡 Key Takeaway

Separating the project into modules makes the workflow easier to:

- understand
- test
- maintain
- debug
- extend

This is particularly useful compared with placing the entire workflow inside one large script or notebook.

---

# 🔄 Finding 10 — The Project Demonstrates an End-to-End ML Workflow

The most important technical outcome of the project is not one individual classifier.

It is the integration of multiple stages into a complete pipeline:

```text
60 Worldwide Locations
          ↓
   REST API Requests
          ↓
     JSON Responses
          ↓
    Raw Data Storage
          ↓
   Data Transformation
          ↓
 Feature Preprocessing
          ↓
   Machine Learning
      ┌─────┴─────┐
      ▼           ▼
Random Forest   Gradient
                Boosting
      │           │
      └─────┬─────┘
            ▼
      Model Evaluation
            ↓
      Results Output
```

### 💡 Key Takeaway

This project demonstrates the transition from simply **training a model** to building the surrounding infrastructure required to collect data, process it, evaluate models and test the application.

---

# 🛠️ Technical Findings

Several broader software and data-science principles emerged from the project.

### 🌐 External Data Sources

REST APIs can be integrated directly into Python pipelines to automate data collection.

### 📦 JSON Processing

API responses must be parsed and transformed into structured analytical datasets.

### 🧹 Data Preparation

Raw information must be validated and transformed before model training.

### 🧠 Model Comparison

Multiple algorithms should be evaluated rather than selecting a model without evidence.

### 🧪 Automated Testing

Pipeline components can be tested independently using PyTest.

### 🎭 Mocking

External API dependencies can be replaced with controlled responses during testing.

### 🔐 Environment Variables

Sensitive credentials should remain separate from source code.

### 🧩 Modular Programming

Separating responsibilities across Python modules makes analytical projects easier to maintain and extend.

---

# ⚠️ Limitations

Several limitations should be considered when interpreting the project.

### Dataset Size

The project collects observations for **60 worldwide locations**, which provides a useful demonstration dataset but remains relatively small for machine-learning purposes.

### AQI Source

The target AQI is obtained from the same external air-pollution data source as the pollutant measurements.

The project should therefore primarily be interpreted as a demonstration of **classification pipeline development** rather than an independent scientific AQI model.

### Model Evaluation

Accuracy alone does not provide a complete assessment of classification performance.

Future evaluation should include:

- precision
- recall
- F1-score
- confusion matrices
- class-level performance

### Geographic Coverage

Although the locations are distributed internationally, 60 locations cannot fully represent global variation in air pollution.

### Temporal Coverage

A larger project would benefit from repeated observations across different times, seasons and environmental conditions.

---

# 🚀 Future Improvements

The project could be extended through:

- 🔁 cross-validation
- 🎛️ hyperparameter optimisation
- 📊 confusion matrices
- 🎯 precision, recall and F1-score
- 🌲 feature-importance analysis
- 📅 historical air-quality data
- ⏱️ repeated or scheduled API collection
- 💾 model persistence
- 🌍 broader geographic coverage
- 📈 interactive visualisations
- 📊 Power BI dashboard integration
- ☁️ cloud deployment
- 🔌 deployment as a prediction API

A future production-style architecture could follow:

```text
Scheduled API Collection
          ↓
Historical Database
          ↓
Automated Processing
          ↓
Trained ML Model
          ↓
Prediction Service
          ↓
Interactive Dashboard
```

---

# 🎯 Overall Conclusion

This project demonstrates a complete **Python machine-learning pipeline from external data collection to model evaluation**.

The strongest technical aspect is the integration of:

```text
REST API
   +
Data Processing
   +
Machine Learning
   +
Modular Python
   +
Automated Testing
   =
End-to-End ML Pipeline
```

Rather than focusing exclusively on model training, the project demonstrates how the surrounding components of a machine-learning application can be designed and connected.

The combination of **API integration, preprocessing, Random Forest and Gradient Boosting classification, automated testing and modular programming** makes this project a practical demonstration of both data-science and Python software-development skills.

---

# 🎓 Academic Context

Originally developed as part of my **MSc Data Science and Its Applications** studies.

For this portfolio repository, the project is presented as an **end-to-end machine-learning engineering case study**, demonstrating the workflow from external API data collection through preprocessing, classification, evaluation and testing.

---

# 👩🏼‍💻 Author

**Julia Legner**  
MSc Data Science and Its Applications  
University of Greenwich

**Portfolio Focus:** Machine Learning • Python • Data Analytics • APIs • Data Science
