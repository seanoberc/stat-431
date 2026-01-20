import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots

Auto = pd.read_csv('Auto.csv', na_values=['?'])
# print(Auto.columns)
# print(Auto["horsepower"].dtype)
# print(Auto["horsepower"].describe())
print(Auto.dtypes)

# The following columns contain the quantitative data in `Auto.csv`:
# print(f"The following columns contain the quantitative data in `Auto.csv`: + {}Auto.columns[:7])


# Auto_new = Auto.dropna()
# print(Auto.shape, Auto_new.shape)
# print(Auto[:4])