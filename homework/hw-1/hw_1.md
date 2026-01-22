---
title: Homework 1
author: Sean Oberc
date: 2026-01-21
geometry: margin-1in
---

$$
\begin{alignedat}{1}
MSE_{test} &= E\left[Y_0 - \hat{f}(x_0)\right]^2 \\
&= E\left[f(x_0) + \epsilon - \hat{f}(x)\right]^2 \\
&= E\left[E[\hat{f}(x_0)] - \hat{f}(x) - E[\hat{f}(x_0)] + f(x_0) + \epsilon\right]^2 \\
&= E\left[\left(E[\hat{f}(x_0)] - \hat{f}(x_0)\right) + \left(f(x_0) - E[\hat{f}(x_0)]\right) + \epsilon\right]^2 \\
&= E\left[\hat{f}(x_0) - E[\hat{f}(x_0)]\right]^2 + \left[f(x_0) - E[\hat{f}(x_0)]\right]^2 + E\left[\epsilon^2\right] \\
&= Var\left(\hat{f}(x_0)\right) \qquad + \qquad Bias^2\left(\hat{f}(x_0)\right) \qquad + \quad Var\left(\epsilon \right)
\end{alignedat}
$$

```{python}
import pandas as pd

auto = pd.read_csv('Auto.csv', na_values = ['?'])
auto = auto.dropna()    # drops the `na_values` in the "horsepower" column--ensures that the predictor is a
                        # unified data type (in this case, a 64-bit floating-point number)

# inspect the columns in the dataset to determine whether a predictor (column) is quantitative or categorical:
print('\n', auto.columns)
print('\n', auto.dtypes)

# print(auto["horsepower"].dtype)
# print(auto["horsepower"].describe())

# range for each set of predictor vals:
# mpg_range = auto["mpg"].max() - auto["mpg"].min()
# cyl_range = auto["cylinders"].max() - auto["cylinders"].min()
# disp_range = auto["displacement"].max() - auto["displacement"].min()
# hp_range = auto["horsepower"].max() - auto["horsepower"].min()
# wt_range = auto["weight"].max() - auto["weight"].min()
# acc_range = auto["acceleration"].max() - auto["acceleration"].min()
# yr_range = auto["year"].max() - auto["year"].min()


cols = ["mpg","cylinders","displacement","horsepower",
        "weight","acceleration","year"]

num = auto.select_dtypes(include = "number")  # selects the relevant predictors from `Auto.csv` by data type
# ranges = (num.max() - num.min()).to_frame("Range")  # assigns the range of each predictor to a var called `ranges`
ranges = (auto[cols].max() - auto[cols].min()).to_frame("Range")    # `.to_frame()` converts the data from a series to a dataframe
print('\n', ranges)



# the `.agg()` function from the `pandas` lib is invoked upon the dataframe (created using `cols`) from Auto.csv; `.T` transposes the rows to columns
summary = auto[cols].agg(["mean", "std"]).T
print('\n', summary)
