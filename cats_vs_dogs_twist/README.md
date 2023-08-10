# Classic Dogs vs. Cats problem in Deep Learning with a twist

# Step 1: Data Collection

1. Access the Kaggle dataset for "Dog Breed Identification" competition: https://www.kaggle.com/c/dog-breed-identification
2. Download all dog images and store them in a directory called "dog-breed-identification".
3. Access the Kaggle dataset for "Dogs vs. Cats" competition: https://www.kaggle.com/c/dogs-vs-cats
4. Download all cat images and store them in a directory called "dogs-vs-cats".

# Step 2: Label Information

1. Obtain the label information from the "label.csv" file in the "Dog Breed Identification" dataset.
2. This file contains dog breed labels corresponding to each image.

# Step 3: Dog Breed Separation

1. Analyze the label information to identify unique dog breeds present in the dataset.
2. Divide the unique dog breeds into two list training and testing.

# Step 4: Organize Dog Images by Breed

1. For each breed in the training, move the corresponding images from the "dog-breed-identification" directory to the "dataset/train/dog" directory.

2. For each breed in the testing, move the corresponding images from the "dog-breed-identification" directory to the "dataset/test/dog" directory.

# Step 5: Cat Image Separation

1. Take only cat images from "dogs-vs-cats" dataset.
2. Divide the cat images into training and testing.
3. Number of cat images is 12500. I have taken 8995 cat images for training and rest 3505 for testing.

# Step 6: Organize Cat Images

1. For each images in the training, move the corresponding images from the "dogs-vs-cats" directory to the "dataset/train/cat" directory.

2. For each breed in the testing, move the corresponding images from the "dogs-vs-cats" directory to the "dataset/test/cat" directory.

# Step 7: Final Dataset Structure

- dataset
  - train
    - dog
      - ...images
    - cat
      - ...images
  - test
    - dog
      - ...images
    - cat
      - ...images

