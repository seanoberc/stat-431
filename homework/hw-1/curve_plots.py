import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)

# squared bias decreases with flexibility
sqr_bias = (1 - x) ** 2

# variance increases with flexibility
variance = x**2

# irreducible error
irr_error = np.full_like(x, 0.20)

# test error
test_error = irr_error + sqr_bias + variance

# training error typically decreases as the model becomes more flexible
training_error = irr_error * 0.6 + 0.9 * (1 - x)**1.5  # purely illustrative

# create a dataframe:
df = pd.DataFrame({
    "Flexibility": x,
    "Squared Bias": sqr_bias,
    "Variance": variance,
    "Training Error": training_error,
    "Test Error": test_error,
    "Irreducible Error": irr_error
})

plt.figure(figsize=(9, 6))

# use the dataframe to plot:
plt.plot(df["Flexibility"], df["Squared Bias"], label="squared bias")
plt.plot(df["Flexibility"], df["Variance"], label="variance")
plt.plot(df["Flexibility"], df["Training Error"], label="training error")
plt.plot(df["Flexibility"], df["Test Error"], label="test error")
plt.plot(df["Flexibility"], df["Irreducible Error"], label="irreducible error")

plt.xlabel("flexibility")
plt.ylabel("error")
plt.title("bias-variance tradeoff")
plt.legend()
plt.grid(True, alpha=0.3)   # shows background grid
plt.ylim(bottom=0)
plt.show()
