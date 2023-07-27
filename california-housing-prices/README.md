# Predicting California Housing Prices using Supervised Regression Methods

In this project, we aimed to predict housing prices in various districts across California using several supervised regression algorithms. We utilized the California Housing Prices dataset sourced from Kaggle, which provides valuable information on district-specific attributes such as population, median income, and median housing price.

# California Housing dataset

The California Housing Prices dataset available on Kaggle, created by user camnugent, provides information on housing prices in various districts across California.

**Data Set Characteristics:**

- Number of Instances: 20640

- Number of Attributes: 10

- Attribute Information:

    - longitude

    - latitude

    - housing_median_age

    - total_rooms

    - total_bedrooms

    - population

    - households

    - median_income

    - median_house_value

    - ocean_proximity

# Workflow 

1. **Data Preprocessing and EDA:**
The dataset is loaded and being analyzed. Find out the missing and handle missing value by drop missing value's rows. One of the biggest impact of Missing Data is, It can bias the results of the machine learning models or reduce the accuracy of the model. So, It is very important to handle missing values.

2. **Linear Regression:**
Linear regression is a simple and widely used regression method that models the relationship between the dependent variable (target) and one or more independent variables (features) as a linear equation. The goal is to find the best-fitting line that minimizes the sum of squared residuals between the predicted and actual values. Linear regression is easy to interpret and computationally efficient. However, it assumes a linear relationship between the variables, which may not always be appropriate for complex data.

3. **Support Vector Regression (SVM):**
Support Vector Regression (SVR) is an extension of the Support Vector Machine (SVM) algorithm for regression tasks. SVR aims to find a hyperplane that best fits the data points while allowing a certain margin of error (epsilon) around the fitted line. It is effective for non-linear regression problems and can handle high-dimensional data. SVR uses kernel functions to transform the data into a higher-dimensional space, where it can find a linear separation. It is particularly useful when the relationship between variables is non-linear.

4. **K-Nearest Neighbors Regression (KNN):**
K-Nearest Neighbors Regression (KNN) is a non-parametric algorithm that predicts the value of a data point by averaging the values of its k-nearest neighbors in the feature space. KNN does not make any assumptions about the underlying data distribution and can handle non-linear relationships between variables. However, it can be sensitive to noisy data and might require careful tuning of the hyperparameter k.

5. **Decision Trees:**
Decision trees are hierarchical tree-like structures that partition the feature space based on different attributes, creating decision rules to make predictions. In regression, each leaf node of the tree contains the predicted value based on the majority of data points in that region. Decision trees are interpretable and can capture complex relationships, but they are prone to overfitting, especially when the tree becomes deep.

6. **Adaboost:**
Adaboost (Adaptive Boosting) is an ensemble learning method that combines weak learners (typically decision trees) to create a strong learner. In each iteration, Adaboost assigns higher weights to misclassified data points, and subsequent learners focus more on those misclassifications. It sequentially builds learners, and their predictions are combined through a weighted majority vote. Adaboost is robust and can improve the performance of weak models.

7. **Multi-layer Perceptron (MLP) Regression:**
Multi-layer Perceptron (MLP) Regression is a type of artificial neural network used for regression tasks. It consists of multiple layers of interconnected nodes (neurons) and can capture complex non-linear relationships in the data. MLPs require more data and computational resources for training but can be highly effective for high-dimensional and non-linear regression problems.

8. **The R-squared (R2) score:**
The R-squared (R2) score, also known as the coefficient of determination, is a statistical measure that quantifies the proportion of the variance in the dependent variable (target) that is explained by the independent variables (features) in a regression model. It is a commonly used evaluation metric for regression tasks. The R2 score ranges from 0 to 1, where:

* R2 = 1 indicates that the regression model perfectly fits the data, capturing all the variability of the dependent variable based on the independent variables. In other words, the model's predictions match the actual data points with no errors.
* R2 = 0 suggests that the regression model does not explain any variability in the dependent variable, and the predictions are equivalent to the mean of the dependent variable.
* R2 < 0 indicates that the model performs worse than predicting the mean, and it might be indicating overfitting.

# Model Evaluation:
For each of the regression algorithms, I trained the models on the training dataset and evaluated their performance on the test dataset. I used the R-squared (R2) score as the evaluation metric to measure the proportion of the variance in the target variable explained by the models' predictions.

# Result:

| Model            | R-squared score | RMSE (train) | RMSE (test)   |
|------------------|-----------------|--------------|---------------|
| Decision Tree    |    0.732212     | 49149.544636 | 60897.025478  |
| Linear Regression|    0.657668     | 68588.643428 | 68853.184759  |
| SVR              |    0.611382     | 72748.959477 | 73360.416507  |
| AdaBoost         |    0.599787     | 74193.840524 | 74446.779120  |
| MLP              |    0.386149     | 91243.192901 | 92200.175667  |
| KNN              |    0.341641     |     0.000000 | 95484.189174  |

Sort by R-squared score

# Best Result:
Based on the R-squared (R2) score, the Decision Tree Regression algorithm achieved the highest performance on the test dataset, with an R-squared score of 0.7322. This score indicates that approximately 73.22% of the variance in housing prices was explained by the Decision Tree model's predictions. As a result, we consider the Decision Tree Regression algorithm as the applicable method for predicting housing prices in California districts in this project.

# Conclusion:
I applied various supervised regression methods to predict California housing prices. The Decision Tree Regression algorithm demonstrated the best performance, achieving an R-squared score of 0.7322 on the test dataset. This model can serve as a valuable tool for predicting housing prices.