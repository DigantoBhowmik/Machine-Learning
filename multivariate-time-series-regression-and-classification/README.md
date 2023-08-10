# Multivariate Time Series Analysis on Household Energy Consumption Dataset with Autoregression and LSTM

## Introduction:
This study presents a comprehensive analysis of a multivariate multi-step time series dataset related to household energy consumption. The analysis focuses on applying two different approaches to forecast energy consumption: Autoregressive (AR) models and Long Short-Term Memory (LSTM) networks. The dataset includes multiple variables, enabling the exploration of complex relationships and patterns within energy consumption data.

## Autoregressive (AR) Models:
The AR model uses the past values of a time series to predict future values. It assumes that the future value depends linearly on its past values and a random error term. The order of the AR model, denoted as AR(p), indicates the number of lagged values used for prediction.

## Long Short-Term Memory (LSTM) Networks:
LSTM is a type of recurrent neural network (RNN) designed to model sequences and time series data. It is well-suited for capturing long-range dependencies in data. LSTM networks contain memory cells that allow them to learn and remember patterns over extended sequences.

## Steps of Analysis:

1. Data Preprocessing:

- Load and inspect the dataset.
- Handle missing values, if any, through interpolation or imputation.
- Normalize the data to ensure all variables are on the same scale.

2. Exploratory Data Analysis (EDA):

- Visualize the time series data to understand trends, seasonality, and potential outliers.
- Explore the relationships between the variables.

3. Feature Engineering:

- Prepare input sequences and corresponding target values for LSTM modeling.
- Split the dataset into training and test sets.
- Remove unnecessary variables from the dataset.
- Add day, month, and year columns to the dataset.

4. Evaluation:

- Evaluate the performance of both Autoregressive and LSTM models using RMSE.
Compare the models' accuracy and generalization capabilities.

5. Prediction and Visualization:

- Make predictions and future prediction using Autoregressive.
- Visualize the predicted energy consumption compared to the actual values using LSTM.

## RMSE Comparison:

1. Autoregression (AR) Model:

- RMSE Value: 0.081558
2. Long Short-Term Memory (LSTM) Network:

- RMSE Value: 0.217640

## Conclusion:
The analysis of the Household Energy Consumption dataset exemplifies the application of Autoregression (AR) and Long Short-Term Memory (LSTM) techniques for time series forecasting. The RMSE comparison reveals that the Autoregression model outperforms the LSTM network, as it exhibits a substantially lower RMSE value. This documentation provides a comprehensive overview of the analysis process, affording readers a comprehensive grasp of the AR and LSTM models' performance in forecasting energy consumption within a multivariate time series context, elucidated through the RMSE metric.

<br><br>

# EEG Eye State Classification

## Introduction:
This study presents an analysis of the EEG Eye State dataset using various machine learning models for classification. The dataset involves EEG measurements and the classification of whether a subject's eyes were open or closed. Four different models were applied: XGBoost, Decision Tree, K-Nearest Neighbors (KNN), and Long Short-Term Memory (LSTM) networks. The primary goal is to compare the performance of these models in classifying eye states based on EEG measurements.

## Dataset:
The EEG Eye State dataset comprises EEG measurements recorded during tasks involving open and closed eyes. Each observation includes multiple features derived from EEG signals. The binary classification task involves predicting whether the subject's eyes were open (1) or closed (0) at a given time.

## Models and Results:

1. XGBoost:

- XGBoost achieved a classification accuracy score of 0.925567.
- XGBoost is an ensemble learning algorithm that combines the predictions of multiple decision trees to improve predictive performance.

2. Decision Tree:

- The Decision Tree model achieved a classification accuracy score of 0.835113.
- Decision Trees are simple yet effective models that partition the feature space based on the features' values.

3. K-Nearest Neighbors (KNN):

- The KNN model achieved a classification accuracy score of 0.827103.
- KNN is a non-parametric classification algorithm that assigns labels based on the majority class among the k-nearest neighbors.

4. Long Short-Term Memory (LSTM) Network:

- The LSTM model achieved a classification accuracy score of 0.529373.
- LSTMs are a type of recurrent neural network (RNN) designed to model sequences and time series data.

## Steps of Analysis:

1. Data Preprocessing:
- Load and inspect the EEG Eye State dataset.
- Check null values

2. Exploratory Data Analysis (EDA):
- Visualize the distributions of EEG measurements for open and closed eye states.
- Analyze correlations among features and their impact on the target variable.

3. Modeling and Evaluation:
- Implement XGBoost, Decision Tree, KNN, and LSTM models.
- Train each model on the dataset and evaluate using accuracy score.

4. Comparison and Conclusion:
- Compare the performance of the four models using their accuracy scores.
- Discuss the strengths and weaknesses of each model in the context of the EEG Eye State classification task.

## Conclusion:
The analysis of the EEG Eye State dataset showcases the performance of different machine learning models in classifying eye states based on EEG measurements. XGBoost demonstrated the highest accuracy score (0.925567), followed by Decision Tree (0.835113), KNN (0.827103), and LSTM (0.529373). The task provides a comprehensive overview of the analysis process, allowing readers to understand the implications of each model's performance in the EEG Eye State classification context and make informed decisions for similar classification tasks.

<br><br>

# Occupancy Detection with ML and DL Methods

## Introduction:
This task presents an analysis of occupancy detection using various machine learning models. The goal is to predict the occupancy status of a space based on provided features. A range of classification models have been applied to the dataset, including K-Nearest Neighbors (KNN), Support Vector Machine (SVM), XGBoost, Decision Tree,  and Long Short-Term Memory (LSTM). This documentation provides insights into the performance of these models in predicting occupancy status.

## Dataset:
The Occupancy Detection dataset contains features related to occupancy and environmental conditions of a space. Each observation includes attributes such as temperature, humidity, and light level. The binary classification task involves predicting whether the space is occupied (1) or unoccupied (0) at a given time.

## K-Nearest Neighbors (KNN):
The KNN model is a non-parametric model that classifies a new data point based on the majority class of its k nearest neighbors. The KNN model is trained using the training set. The model is then used to predict the occupancy status of the testing set. The accuracy of the model is then calculated by comparing the predicted labels to the actual labels of the testing set. The accuracy of the KNN model is 0.98.

## Support Vector Machine (SVM):
The SVM model is a supervised learning model that classifies a new data point based on its position relative to a hyperplane. The SVM model is trained using the training set. The model is then used to predict the occupancy status of the testing set. The accuracy of the model is then calculated by comparing the predicted labels to the actual labels of the testing set. The accuracy of the SVM model is 0.975.

## XGBoost:
The XGBoost model is an ensemble learning model that uses a gradient boosting framework. The XGBoost model is trained using the training set. The model is then used to predict the occupancy status of the testing set. The accuracy of the model is then calculated by comparing the predicted labels to the actual labels of the testing set. The accuracy of the XGBoost model is 0.94.

## Decision Tree:
The Decision Tree model is a supervised learning model that uses a tree-like structure to classify a new data point. The Decision Tree model is trained using the training set. The model is then used to predict the occupancy status of the testing set. The accuracy of the model is then calculated by comparing the predicted labels to the actual labels of the testing set. The accuracy of the Decision Tree model is 0.82.

## Long Short-Term Memory (LSTM):
The LSTM model is a recurrent neural network that uses a memory cell to classify a new data point. The LSTM model is trained using the training set. The model is then used to predict the occupancy status of the testing set. The accuracy of the model is then calculated by comparing the predicted labels to the actual labels of the testing set. The accuracy of the LSTM model is 0.84.

## Conclusion:
The Occupancy Detection Model Comparison analysis provides valuable insights into the performance of various classification models. KNN and SVM demonstrated the highest accuracy scores, closely followed by XGBoost. The documentation offers a comprehensive view of the comparison process, aiding readers in understanding the strengths and weaknesses of each model's performance in predicting occupancy status. This knowledge enables informed decision-making when selecting the most suitable model for occupancy detection scenarios.