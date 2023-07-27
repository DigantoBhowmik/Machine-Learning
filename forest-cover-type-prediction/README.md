# Title: Forest Cover Type Prediction using Supervised Classification Methods and Ensemble Classifier

# Introduction:
In this project, I aimed to predict forest cover types based on various attributes using several supervised classification algorithms. The Forest Cover Type Prediction dataset was used for this analysis. After performing Exploratory Data Analysis (EDA) to understand the dataset's structure and relationships, I employed various classification methods, including Linear Classification, SVM, KNN Classification, Decision Trees, Adaboost and MLP. Additionally, I created an Ensemble Classifier using the top 3 and top 5 performing models to improve predictive accuracy.

# Dataset Description:
The Forest Cover Type Prediction dataset contains information on various attributes of forested areas. Each instance represents a 30x30-meter cell, and the attributes include elevation, aspect, slope, soil type, wilderness area, and other relevant features. The target variable is the forest cover type, categorized into seven classes representing different types of trees present in the area.

**Four wilderness areas are:**

1. Rawah
2. Neota
3. Comanche Peak
4. Cache la Poudre

**Seven categories numbered from 1 to 7 in the Cover_Type column:**

1. Spruce/Fir
2. Lodgepole Pine
3. Ponderosa Pine
4. Cottonwood/Willow
5. Aspen
6. Douglas-fir
7. Krummholz


# Exploratory Data Analysis (EDA):
During EDA, I explored the dataset's descriptive statistics, visualized feature distributions, and assessed the correlation betIen features and the target variable. I handled any missing data, identified potential outliers, and performed data preprocessing to ensure the dataset was ready for training and evaluation.

# Supervised Classification Methods:
I employed various supervised classification algorithms to predict forest cover types:

1. Linear Classification: Utilized linear models such as Logistic Regression or Linear SVM.
2. SVM Classification: Implemented the Support Vector Machine algorithm for classification tasks.
3. KNN Classification: Applied the K-Nearest Neighbors algorithm for classification.
4. Decision Tree Classification: Used Decision Trees for building a classification model.
5. Adaboost Classification: Employed the AdaBoost ensemble method for classification.
6. MLP Classification: Trained a Multi-Layer Perceptron (Neural Network) for classification.

# Model Evaluation:
For each classification algorithm, I split the dataset into training and test sets. I trained the models on the training set and evaluated their performance on the test set using the accuracy_score metric. The accuracy_score measures the percentage of correct predictions over the total number of instances.

# Result

| Model          | Score      |
|----------------|------------|
| KNN            | 0.814437   |
| Decision Tree  | 0.795677   |
| MLP            | 0.783034   |
| SVM            | 0.730016   |
| Linear         | 0.649266   |
| AdaBoost       | 0.449837   |

# Model Performance Analysis:

1. KNN:

- KNN achieved the highest accuracy score of 81.44% among all the models.
- Its non-parametric nature enables it to capture complex relationships in the data.
- KNN's high accuracy suggests that it is well-suited for predicting forest cover types in this context.

2. Decision Tree:

- The Decision Tree model exhibited strong performance with an accuracy score of 79.57%.
- Decision Trees are effective at handling both numerical and categorical features, making them suitable for this dataset.

3. MLP (Multi-Layer Perceptron):

- MLP showed competitive performance with an accuracy score of 78.30%.
- As a neural network-based model, MLP can learn intricate patterns in the data, leading to strong predictive capabilities.

4. SVM (Support Vector Machine):

- SVM achieved an accuracy score of 73.00%.
- Although SVM is a powerful classifier, it may require further hyperparameter tuning to improve its performance in this context.

5. Linear SVC:

- Linear demonstrated an accuracy score of 64.93%.
- Linear may be more suitable for linearly separable datasets and could benefit from additional feature engineering or preprocessing.

6. AdaBoost:

- AdaBoost achieved the lowest accuracy score of 44.98%.
- AdaBoost is an ensemble method that combines weak learners, but its performance on this dataset suggests it may not be the best fit.

# Ensemble Classifier - Top 3 Models:
I created an Ensemble Classifier by combining the predictions from the top three performing models - KNN, Decision Tree, and MLP - using majority voting. The Ensemble Classifier achieved an impressive accuracy score of 84%.

# Ensemble Classifier - Top 5 Models:
Similarly, for the Ensemble Classifier with the top five models - KNN, Decision Tree, MLP, SVM, and Linear- I applied majority voting. The Ensemble Classifier achieved an accuracy score of 80%.

# Conclusion:
In this project, I employed several supervised classification algorithms to predict forest cover types based on the Forest Cover Type Prediction dataset. KNN outperformed other models, achieving an accuracy score of 81.44%. The Decision Tree and MLP models also demonstrated competitive performance with accuracy scores of 79.57% and 78.30%, respectively.

The Ensemble Classifiers, both with the top 3 and top 5 models, significantly improved predictive accuracy, achieving 84% and 80% accuracy, respectively. This demonstrates the potential of leveraging multiple models to enhance the predictive capabilities of the classifiers.
