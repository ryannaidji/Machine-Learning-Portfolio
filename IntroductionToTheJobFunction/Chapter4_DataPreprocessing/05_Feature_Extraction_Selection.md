# Feature Extraction and Selection

## What is Feature Extraction?
- Among the important aspects of machine learning, feature extraction and selection are crucial.
- Feature extraction allows us to obtain a set of informative variables.
- For example, if we want to model the weather, the date, temperature, humidity, and wind speed are informative (they are related to the problem). However, the result of a football match will not be an informative feature as it does not affect the weather.

## What is Feature Selection?
- It involves selecting a subset of features that will be used to train the learning algorithm, i.e., relevant features.
- The selected features will be used, and all others will be ignored, reducing dimensionality.
- In the previous example, we may realize that with climate change, the date is no longer a relevant feature and that only temperature, humidity, and wind speed are relevant features.

## Feature Selection: Formalization
- Given a set of features $F = \{f_1, f_2, \ldots, f_n\}$, feature selection consists of determining a subset that maximizes the model's ability to characterize forms, i.e., determining the subset $F'$ that maximizes the cost function.

## Why Feature Selection?
- It allows the machine learning algorithm to train faster.
- Reduces the complexity of a model and makes it easier to interpret.
- Improves the accuracy of a model if a subset of relevant features is chosen.
- Reduces overfitting.
