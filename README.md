<div align=”center”><img src="https://user-images.githubusercontent.com/46392391/92135137-0187c900-ee28-11ea-9bd9-7079c5c93f95.png" height="250"><div>

# [freeCodeCamp Machine Learning with Python Projects](https://www.freecodecamp.org/learn)

<div align=”center”><img src="https://user-images.githubusercontent.com/46392391/92091023-c9fc2b00-eded-11ea-87ab-8c0997081eb0.png" height="250"><div>

## 1. [Rock Paper Scissors](RockPaperScissor/)

For this challenge, you will create a program to play Rock, Paper, Scissors. A program that picks at random will usually win 50% of the time. To pass this challenge your program must play matches against four different bots, winning at least 60% of the games in each match.

In the file `RPS.py` you are provided with a function called `player`. The function takes an argument that is a string describing the last move of the opponent ("R", "P", or "S"). The function should return a string representing the next move for it to play ("R", "P", or "S").

A player function will receive an empty string as an argument for the first game in a match since there is no previous play.

The file `RPS.py` shows an example function that you will need to update. The example function is defined with two arguments (`player(prev_play, opponent_history = [])`). The function is never called with a second argument so that one is completely optional. The reason why the example function contains a second argument (`opponent_history = []`) is because that is the only way to save state between consecutive calls of the `player` function. You only need the `opponent_history` argument if you want to keep track of the opponent_history.

*Hint: To defeat all four opponents, your program may need to have multiple strategies that change depending on the plays of the opponent.*

<div align=”center”><img src="https://user-images.githubusercontent.com/46392391/92091018-c9639480-eded-11ea-97a1-fd1d93ea9fe6.jpeg" height="250"><div>

## 2. [Cat and Dog Image Classifier](CatDogClassifier/fcc_cat_dog.ipynb)

For this challenge, you will complete the code below to classify images of dogs and cats. You will use Tensorflow 2.0 and Keras to create a convolutional neural network that correctly classifies images of cats and dogs at least 63% of the time. (Extra credit if you get it to 70% accuracy!)

Some of the code is given to you but some code you must fill in to complete this challenge. Read the instruction in each text cell so you will know what you have to do in each code cell.

The first code cell imports the required libraries. The second code cell downloads the data and sets key variables. The third cell is the first place you will write your own code.

The structure of the dataset files that are downloaded looks like this (You will notice that the test directory has no subdirectories and the images are not labeled):
```
cats_and_dogs
|__ train:
    |______ cats: [cat.0.jpg, cat.1.jpg ...]
    |______ dogs: [dog.0.jpg, dog.1.jpg ...]
|__ validation:
    |______ cats: [cat.2000.jpg, cat.2001.jpg ...]
    |______ dogs: [dog.2000.jpg, dog.2001.jpg ...]
|__ test: [1.jpg, 2.jpg ...]
```

You can tweak epochs and batch size if you like, but it is not required.

<div align=”center”><img src="https://user-images.githubusercontent.com/46392391/92091014-c799d100-eded-11ea-8e84-01e851fdaadd.jpeg" height="250"><div>

## 3. [Book Recommendation Engine using KNN](Book%Recommender/fcc_book_recommendation_knn.ipynb)

In this challenge, you will create a book recommendation algorithm using **K-Nearest Neighbors**.

You will use the [Book-Crossings dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/). This dataset contains 1.1 million ratings (scale of 1-10) of 270,000 books by 90,000 users. 

After importing and cleaning the data, use `NearestNeighbors` from `sklearn.neighbors` to develop a model that shows books that are similar to a given book. The Nearest Neighbors algorithm measures distance to determine the “closeness” of instances.

Create a function named `get_recommends` that takes a book title (from the dataset) as an argument and returns a list of 5 similar books with their distances from the book argument.

This code:

`get_recommends("The Queen of the Damned (Vampire Chronicles (Paperback))")`

should return:

```
[
  'The Queen of the Damned (Vampire Chronicles (Paperback))',
  [
    ['Catch 22', 0.793983519077301], 
    ['The Witching Hour (Lives of the Mayfair Witches)', 0.7448656558990479], 
    ['Interview with the Vampire', 0.7345068454742432],
    ['The Tale of the Body Thief (Vampire Chronicles (Paperback))', 0.5376338362693787],
    ['The Vampire Lestat (Vampire Chronicles, Book II)', 0.5178412199020386]
  ]
]
```
I used https://datascienceplus.com/building-a-book-recommender-system-the-basics-knn-and-matrix-factorization/ for help.

<div align=”center”><img src="https://user-images.githubusercontent.com/46392391/92113719-5d912400-ee0d-11ea-9862-a1fdb9b0b957.jpeg" height="250"><div>

## 4. [Linear Regression Health Costs Calculator](PredictHealthcare/predict_health_costs_with_regression.ipynb)

In this challenge, you will predict healthcare costs using a regression algorithm.

You are given a dataset that contains information about different people including their healthcare costs. Use the data to predict healthcare costs based on new data.

The first two cells of this notebook import libraries and the data.

Make sure to convert categorical data to numbers. Use 80% of the data as the train_dataset and 20% of the data as the test_dataset.

pop off the "expenses" column from these datasets to create new datasets called train_labels and test_labels. Use these labels when training your model.

Create a model and train it with the train_dataset. Run the final cell in this notebook to check your model. The final cell will use the unseen test_dataset to check how well the model generalizes.

To pass the challenge, model.evaluate must return a Mean Absolute Error of under 3500. This means it predicts health care costs correctly within $3500.

The final cell will also predict expenses using the test_dataset and graph the results.

Help from:

https://www.tensorflow.org/tutorials/keras/regression

https://medium.com/@BAYUGALIH/prediction-of-health-insurance-costs-with-linear-regression-8fd95a905a40

<div align=”center”><img src="https://user-images.githubusercontent.com/46392391/92134803-9a6a1480-ee27-11ea-95ce-a965a2aaf06a.png" height="250"><div>

## 5. [Neural Network SMS Text Classifier](SMSclassifier/fcc_sms_text_classification.ipynb)

In this challenge, you need to create a machine learning model that will classify SMS messages as either "ham" or "spam". A "ham" message is a normal message sent by a friend. A "spam" message is an advertisement or a message sent by a company.

You should create a function called predict_message that takes a message string as an argument and returns a list. The first element in the list should be a number between zero and one that indicates the likeliness of "ham" (0) or "spam" (1). The second element in the list should be the word "ham" or "spam", depending on which is most likely.

For this challenge, you will use the SMS Spam Collection dataset. The dataset has already been grouped into train data and test data.
