# Continuous Dependent Variable: Regression

In this section, we will cover the concept of regression when the dependent variable is continuous. We will explore different types of regression techniques, including linear regression, polynomial regression, regression with basis functions, and regularization methods.

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

**Ridge Regression** adds a penalty equal to the sum of the squared coefficients (L2 norm) to the loss function. The objective function is:

$$Minimize \sum_{i=1}^n (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^p \beta_j^2 $$

where $\lambda$ is the regularization parameter that controls the strength of the penalty.

### Lasso Regression

**Lasso Regression** adds a penalty equal to the sum of the absolute values of the coefficients (L1 norm) to the loss function. The objective function is:

$$\text{Minimize } \sum_{i=1}^n (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^p |\beta_j|$$

Lasso can set some coefficients to zero, effectively performing feature selection.

### Elastic Net

**Elastic Net** combines the penalties of Ridge and Lasso. The objective function is:

$$\text{Minimize } \sum_{i=1}^n (y_i - \hat{y}_i)^2 + \lambda_1 \sum_{j=1}^p |\beta_j| + \lambda_2 \sum_{j=1}^p \beta_j^2$$

Elastic Net is useful when there are multiple features that are correlated with one another.
