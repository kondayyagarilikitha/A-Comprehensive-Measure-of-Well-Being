# 🌍 HDI Well-Being Predictor

An AI-powered web application that predicts the **Human Development Index (HDI)** using Machine Learning. The project is developed using **Python, Flask, Scikit-learn, HTML, CSS, JavaScript, and Chart.js** to provide an interactive dashboard for analyzing well-being indicators.

---

## 📌 Project Overview

The Human Development Index (HDI) is a comprehensive measure of a country's overall well-being based on health, education, and income indicators.

This application predicts the HDI value using a trained **Linear Regression** model and classifies countries into different human development categories.

The project also provides an interactive dashboard with data visualization, prediction analysis, and model information.

---

## 🎯 Objectives

- Predict Human Development Index (HDI) using Machine Learning.
- Analyze well-being indicators.
- Provide an interactive dashboard for users.
- Visualize input indicators using graphs.
- Deploy the trained model through a Flask web application.

---

# ✨ Features

- 🌍 Interactive Dashboard
- 🤖 Machine Learning Prediction
- 📊 HDI Score Prediction
- 🏷️ Human Development Category Classification
- 📈 Indicator Visualization using Charts
- 📉 Animated HDI Progress Bar
- 📋 Model Information Panel
- 🎨 Responsive User Interface
- ⚡ Fast Prediction using Flask

---

# 🛠 Technologies Used

### Programming Languages

- Python
- HTML5
- CSS3
- JavaScript

### Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Flask

### Machine Learning

- Linear Regression

### Visualization

- Chart.js

---

# 📂 Project Structure

```
Wellbeing Predictor
│
├── app.py
├── train.py
├── requirements.txt
│
├── data
│   ├── hdi.csv
│   └── hdi_clean.csv
│
├── model
│   ├── hdi_model.pkl
│   └── metrics.pkl
│
├── templates
│   └── dashboard.html
│
├── static
│   ├── style.css
│   ├── dashboard.js
│   └── images
│
└── README.md
```

---

# ⚙️ Machine Learning Workflow

## Epic 1

Environment Setup

- Install required Python packages
- Create project structure

---

## Epic 2

Import Required Libraries

- Pandas
- NumPy
- Flask
- Matplotlib
- Scikit-learn
- Joblib

---

## Epic 3

Dataset Understanding

- Load Kaggle HDI Dataset
- Explore dataset
- Analyze features
- Visualize data

---

## Epic 4

Data Preprocessing

- Handle missing values
- Select features
- Clean dataset
- Create training dataset

---

## Epic 5

Train-Test Split

- 80% Training
- 20% Testing

---

## Epic 6

Model Development

- Linear Regression
- Train Model
- Predict HDI
- Evaluate Performance

---

## Epic 7

Model Saving

- Save trained model (.pkl)
- Save evaluation metrics

---

## Epic 8

Flask Deployment

- Interactive Dashboard
- User Input Form
- Prediction System
- Visualization
- Responsive Interface

---

# 📊 Input Features

- Life Expectancy
- Expected Years of Schooling
- Mean Years of Schooling
- Gross National Income (GNI) per Capita

---

# 📈 Output

The application predicts:

- HDI Score
- Human Development Category

Categories include:

- Low Human Development
- Medium Human Development
- High Human Development
- Very High Human Development

---

# 📊 Dashboard Components

- HDI Prediction Card
- Category Display
- Progress Indicator
- Indicator Visualization Chart
- Model Information Panel

---

# 🚀 Installation

Clone the repository

```bash
git clone <repository_link>
```

Move into project folder

```bash
cd Wellbeing-Predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train.py
```

Run Flask

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📷 Project Demo

The dashboard provides:

- Interactive prediction interface
- Machine learning prediction
- Dynamic progress visualization
- Indicator charts
- Responsive design
- Model information

---

# 🔮 Future Enhancements

- Country Selection
- World HDI Comparison
- Multiple ML Algorithms
- Feature Importance Analysis
- PDF Report Generation
- Cloud Deployment
- User Authentication
- Historical HDI Trends
- AI-based Recommendation System

---

# 📚 Dataset

Human Development Index (HDI) Dataset

Source: Kaggle

