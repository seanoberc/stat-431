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

# create and print a table for the range values:
# range_table = pd.DataFrame({
#     "Range": [
#         mpg_range,
#         cyl_range,
#         disp_range,
#         hp_range,
#         wt_range,
#         acc_range,
#         yr_range
#     ]
# }, index = [
#     "mpg",
#     "cylinders",
#     "displacement",
#     "horsepower",
#     "weight",
#     "acceleration",
#     "year"
# ])
# print(range_table)

cols = ["mpg","cylinders","displacement","horsepower",
        "weight","acceleration","year"]

num = auto.select_dtypes(include = "number")  # selects the relevant predictors from `Auto.csv` by data type
# ranges = (num.max() - num.min()).to_frame("Range")  # assigns the range of each predictor to a var called `ranges`
ranges = (auto[cols].max() - auto[cols].min()).to_frame("Range")    # `.to_frame()` converts the data from a series to a dataframe
print('\n', ranges)

# finds and prints the mean and standard deviation for each range:
# num = auto.select_dtypes(include = "number")
# summary = pd.DataFrame({
#     "Mean": num.mean(),
#     "Std Dev": num.std()
# })
# print('\n', summary)

# the `.agg()` function from the `pandas` lib is invoked upon the dataframe (created using `cols`) from Auto.csv; `.T` transposes the rows to columns
summary = auto[cols].agg(["mean", "std"]).T
print('\n', summary)

