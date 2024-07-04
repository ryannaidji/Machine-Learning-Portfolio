# Introduction

## 1. Contextualization

- Some regression algorithms can be used for classification.
- Logistic regression (also known as logit regression) determines the probability that an observation belongs to a particular class.
- Logistic regression provides the probability of the outcome (logistic of the outcome) instead of the outcome itself.
- In other words, in logistic regression, it is not the binary response (sick/not sick) that is directly modeled, but the probability of one of the two modalities occurring (e.g., being sick).
- If the estimated probability is greater than 50%, the model predicts that the observation belongs to the positive class labeled "1".
- Otherwise, it predicts that the observation belongs to the negative class labeled "0".
- Examples of applications of the binomial logistic regression model:
  - Purchase or not of a product
  - Good or bad customer
  - Failure or success in an exam
  - Absence or presence of a pathology

## 2. Review of the Linear Regression Model

A linear model makes a prediction by simply calculating a weighted sum of the input variables and adding a constant term:

---


>$$\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \ldots + \theta_n x_n$$

Where:
- $\hat{y}$ is the predicted value
- $n$ is the number of variables
- $\theta_n$ is the $n$ th parameter of the model


---
The equation can be written in a general form (vector form):

---


>$$\hat{y} = h_\theta (x) = \theta \cdot x$$

Where:
- $\theta$ is the parameter vector of the model, containing both $\theta_0$ and the weight coefficients $\theta_1$ to $\theta_n$ of the variables
- $x$ is the vector of values of an observation, containing the values $x_0$ to $x_n$, where $x_0$ is always equal to 1.
- $\theta \cdot x$ is the dot product of $\theta$ and $x$.


---

* The difference between linear regression and logistic regression is that the latter provides the probability of the outcome (logistic of the outcome) instead of the outcome itself.
* The probability estimated by the logistic regression model is:
---


>$$\hat{p} = h_\theta (x) = \rho (x^T \theta)$$

Where:
- $\rho$ is a sigmoid function


---

The question is: How to estimate these probabilities?
