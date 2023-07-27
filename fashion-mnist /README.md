## Unsupervised Methods for Fashion MNIST

This project explores various unsupervised learning techniques on the Fashion MNIST dataset The goal is to apply dimensionality reduction and clustering algorithms to identify patterns and group similar fashion items together.

# Dataset

Fashion MNIST is a collection of 28x28 pixel images, each corresponding to a specific fashion item. The dataset contains 10 classes, including items like T-shirts, trousers, dresses, and more.

# Workflow

1. **Load the Dataset:** Load the Fashion MNIST dataset.

2. **t-SNE Visualization:** Apply t-SNE to reduce the data's dimensionality to 2D and visualize the reduced data using a scatter plot.

3. **K-Means Clustering:** Perform K-Means clustering on the original data. Tune hyperparameters like n_init and max_iter to optimize results.

4. **PCA (Principal Component Analysis):** Reduce the data's dimensionality using PCA.

5. **K-Means on PCA-Processed Data:** Perform K-Means clustering on the reduced data obtained from PCA.

6. **SVD (Singular Value Decomposition):** Reduce the data's dimensionality using SVD. 

7. **K-Means on SVD-Processed Data:** Perform K-Means clustering on the reduced data obtained from SVD.

8. **Truncated SVD:** Reduce the data's dimensionality using Truncated SVD. 

9. **K-Means on Truncated SVD-Processed Data:** Perform K-Means clustering on the reduced data obtained from Truncated SVD.

10. **ICA (Independent Component Analysis):** Reduce the data's dimensionality using ICA. 

11. **K-Means on ICA-Processed Data:** Perform K-Means clustering on the reduced data obtained from ICA.