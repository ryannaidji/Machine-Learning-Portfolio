# Continuous Dependent Variable: Regression

In this section, we will cover the concept of regression when the dependent variable is continuous. We will explore different types of regression techniques, including linear regression, polynomial regression, regression with basis functions, and regularization methods.

## Continuous Variable

A **continuous variable** is a variable that can take any value within a given range. These values are not restricted to specific discrete categories but can be any value, including fractions and decimals. Examples of continuous dependent variables include:

- Temperature (e.g., 23.5°C, 37.8°C)
- Price (e.g., $19.99, $100.50)
- Height (e.g., 175.3 cm, 160.0 cm)
- Time (e.g., 5.67 seconds, 10.3 minutes)

## Continuous Dependent Variable

In the context of supervised learning, a **continuous dependent variable** is a continuous variable that we aim to predict.

- Predicting the temperature based on various weather parameters.
- Estimating the price of a house based on its features such as size, location, and number of rooms.
- Determining the height of a person based on their age and other factors.
- Forecasting the time required to complete a task based on its complexity and other factors.

## Linear Regression

**Linear Regression** is the simplest form of regression. It assumes a linear relationship between the dependent variable $y$ and one or more independent variables $x$. The relationship is modeled by a linear equation:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \ldots + \beta_n x_n$$

where:
- $y$ is the dependent variable
- $x_1, x_2, \ldots, x_n$ are the independent variables
- $\beta_0, \beta_1, \ldots, \beta_n$ are the coefficients to be estimated

## Polynomial Regression

**Polynomial Regression** extends linear regression by allowing for polynomial terms of the independent variables. This can capture non-linear relationships. The model takes the form:

$$y = \beta_0 + \beta_1 x + \beta_2 x^2 + \ldots + \beta_d x^d$$

where $d$ is the degree of the polynomial.

## Regression with Basis Functions

**Regression with Basis Functions** involves transforming the original features into a new set of features using basis functions. This allows for more flexible models that can capture complex relationships. Common basis functions include polynomial, Gaussian, and spline functions.

## Regularization

**Regularization** techniques are used to prevent overfitting by adding a penalty to the model coefficients. The two most common regularization techniques are Ridge and Lasso, and their combination, Elastic Net.

### Ridge Regression

**Ridge Regression** is a regularization technique that adds a penalty to the size of the coefficients. This helps to prevent overfitting by shrinking the coefficients towards zero.

### Lasso Regression

**Lasso Regression** is another regularization technique that adds a penalty to the absolute values of the coefficients. It can set some coefficients to zero, effectively performing feature selection.

### Elastic Net

**Elastic Net** combines the penalties of both Ridge and Lasso. It is useful when there are multiple features that are correlated with one another.
