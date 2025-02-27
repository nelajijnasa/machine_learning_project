🌍 Overview

This project automates the extraction of species data from the IUCN Red List using Selenium and predicts the endangerment status of species using Machine Learning. The trained model is deployed as an API using Microsoft Azure Functions.

🚀 Features

✅ Automated Web Scraping – Extracts species data from the IUCN Red List website.

🤖 Machine Learning Model – Predicts species' endangerment status using a Multiclass Boosted Decision Tree.

☁️ Azure Deployment – REST API for real-time predictions.

📊 Data Processing – Cleans and prepares the dataset for analysis.

🔎 Multiple Conservation Categories – Classifies species as Least Concern, Vulnerable, Endangered, Critically Endangered, or Extinct.

📂 Repository Structure

📦 iucn-species-predictor
│-- 📂 data/                  # Dataset and processed data
│   ├── scraped_data.csv       # Data collected using Selenium
│   ├── cleaned_data.csv       # Preprocessed dataset for ML
│
│-- 📂 models/                # Machine learning models
│   ├── model.pkl             # Trained model (saved)
│   ├── model_metadata.json    # Model details (features, parameters)
│
│-- 📂 notebooks/             # Jupyter Notebooks for analysis
│   ├── EDA.ipynb             # Exploratory Data Analysis
│   ├── Training.ipynb        # Model training steps
│   ├── Evaluation.ipynb      # Model evaluation
│
│-- 📂 scripts/               # Python scripts for automation
│   ├── scraper.py            # Selenium-based web scraper
│   ├── preprocess.py         # Data cleaning & preprocessing
│   ├── train_model.py        # ML model training
│   ├── predict.py            # ML model inference
│
│-- 📂 deployment/            # Azure deployment files
│   ├── azure_function.py     # Azure Function script
│   ├── requirements.txt      # Python dependencies
│   ├── Dockerfile            # Docker setup (if used)
│
│-- 📂 docs/                  # Documentation & reports
│   ├── project_report.pdf    # Your full project report
│   ├── architecture.png      # System architecture diagram
│
│-- .gitignore                # Ignore unnecessary files
│-- README.md                 # Main project documentation
│-- requirements.txt          # Python dependencies
│-- LICENSE                   # (Optional) Open-source license

⚡ Installation & Setup

🛠 Prerequisites

Python 3.8+ installed

Install required libraries:

pip install -r requirements.txt

🔥 Clone Repository

git clone https://github.com/yourusername/iucn-species-predictor.git
cd iucn-species-predictor

🚀 Run Scripts

1️⃣ Run the Web Scraper

python scripts/scraper.py

2️⃣ Train the Machine Learning Model

python scripts/train_model.py

3️⃣ Predict Species Status

python scripts/predict.py --species "Tiger"

☁️ Azure Deployment

The trained model is deployed using Azure Functions to provide a REST API for real-time predictions.

Steps to Deploy:

Create an Azure Function App.

Upload azure_function.py as the main function.

Configure the requirements.txt to install dependencies.

Deploy using:

az functionapp deployment source config-zip -g <resource-group> -n <function-app-name> --src function.zip

Use Postman or a frontend app to interact with the API.

Example API Input (JSON)

{
  "habitat": "Forest",
  "num_threats": 5,
  "category": "Mammal",
  "generation_length": 12
}

Example API Output (Prediction)

{
  "predicted_status": "Endangered"
}

📊 Model Performance

Algorithm Used: Multiclass Boosted Decision Tree

Accuracy: 61%

Precision (Macro): 42.53%

Recall (Macro): 39.8%

📌 Future Work

🔹 Improve Model Performance – Try advanced deep learning m
