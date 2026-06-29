# House Price Prediction using Decision Tree Regressor

## Overview
This project predicts house prices using the Decision Tree Regression algorithm. The model is trained on house-related features such as area type, location, BHK, total square feet, bathrooms, and balconies to estimate the selling price of a house.

## Problem Statement
House prices vary based on several factors such as location, size, and amenities. Predicting house prices manually is difficult and time-consuming. This project uses Machine Learning to build a model that predicts house prices accurately.

## Objectives
- Predict house prices using Machine Learning.
- Perform data preprocessing and cleaning.
- Train a Decision Tree Regressor model.
- Evaluate the model using R² Score and Mean Absolute Error.

## Dataset Features
- Area Type
- Availability
- Location
- BHK
- Total Square Feet
- Bathrooms
- Balconies
- Price (Target Variable)

## Technologies Used
- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Project Workflow
1. Import required libraries.
2. Load the dataset.
3. Clean and preprocess the data.
4. Encode categorical features.
5. Split the dataset into training and testing sets.
6. Train the Decision Tree Regressor model.
7. Predict house prices.
8. Evaluate model performance.

## Model
- Algorithm: Decision Tree Regressor
- Random State: 50

## Evaluation Metrics
- R² Score
- Mean Absolute Error (MAE)

## Results
The Decision Tree Regressor model successfully predicts house prices based on the given input features. The performance is evaluated using R² Score and MAE.

## Folder Structure
```
House-Price-Prediction/
│
├── House_Price_Prediction.ipynb
├── House_Price_Dataset.csv
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install pandas numpy matplotlib scikit-learn
```

## Run the Project

1. Open the notebook in Google Colab or Jupyter Notebook.
2. Upload the dataset.
3. Run all cells.
4. View the predicted house prices and evaluation metrics.

## Future Enhancements
- Improve prediction accuracy using Random Forest and XGBoost.
- Deploy the model as a web application.
- Add more features such as age of property and parking.

## Author
**Keerthi Yerradasari**

## License
This project is for educational purposes.
