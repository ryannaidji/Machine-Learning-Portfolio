# Introduction to DataFrames and Variables

In this section, we will introduce the basic concepts of DataFrames and the variables involved in regression and linear modeling. We will cover the structure of a DataFrame, the definitions of independent and dependent variables, and provide an example using Pandas.

## Structure of a DataFrame

A DataFrame is a two-dimensional labeled data structure with columns of potentially different types. It can be thought of as a table or spreadsheet in which rows and columns are indexed.

### Axes in a DataFrame

- **Axis 0**: Refers to the rows.
- **Axis 1**: Refers to the columns.

## Independent Variables (Features, Descriptors, Predictors, $x_i$)

Independent variables, also known as features, descriptors, or predictors, are the input variables used to predict the target variable. These variables are denoted as $x_i$, where $i$ can be any integer representing different features.

## Dependent Variable (Target, $y$)

The dependent variable, also known as the target, is the output variable that we aim to predict. This variable is denoted as $y$.

## Example DataFrame with Pandas

Let's look at an example of how a DataFrame is structured and how independent and dependent variables are represented using Pandas in Python:

```python
import pandas as pd

# Example data
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [5, 4, 3, 2, 1],
    'Target': [1.1, 1.9, 3.0, 3.9, 5.1]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
```

The above code creates a simple DataFrame with two features (`Feature1` and `Feature2`) and one targot variable (`Target`). The DataFrame looks like this:

The above code creates a simple DataFrame with two features (`Feature1` and `Feature2`) and one target variable (`Target`). The DataFrame looks like this:

|   | Feature1 | Feature2 | Target |
|---|----------|----------|--------|
| 0 | 1        | 5        | 1.1    |
| 1 | 2        | 4        | 1.9    |
| 2 | 3        | 3        | 3.0    |
| 3 | 4        | 2        | 3.9    |
| 4 | 5        | 1        | 5.1    |

In this example, `Feature1` and `Feature2` are the independent variables $x_1$ and $x_2$, and `Target` is the dependent variable $y$.

---
