import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# X-axis: "flexibility" (low -> high)
x = np.linspace(0, 1, 400)

# --- Construct typical conceptual curves ---
# Squared bias: decreases with flexibility
bias2 = (1 - x)**2

# Variance: increases with flexibility
variance = x**2

# Bayes / irreducible error: constant (horizontal line)
bayes = np.full_like(x, 0.20)

# Test error: U-shaped = bayes + bias^2 + variance (often shown this way)
test_error = bayes + bias2 + variance

# Training error: typically decreases with flexibility (often below test error)
# We'll make it decrease smoothly toward something near 0 (but not negative).
training_error = bayes * 0.6 + 0.9 * (1 - x)**1.5  # purely illustrative

# Put into a DataFrame (optional, but nice if you want to inspect values)
df = pd.DataFrame({
    "Flexibility": x,
    "Squared Bias": bias2,
    "Variance": variance,
    "Training Error": training_error,
    "Test Error": test_error,
    "Bayes Error": bayes
})

# --- Plot ---
plt.figure(figsize=(9, 6))

plt.plot(df["Flexibility"], df["Squared Bias"], label="Squared Bias")
plt.plot(df["Flexibility"], df["Variance"], label="Variance")
plt.plot(df["Flexibility"], df["Training Error"], label="Training Error")
plt.plot(df["Flexibility"], df["Test Error"], label="Test Error")
plt.plot(df["Flexibility"], df["Bayes Error"], label="Bayes (Irreducible) Error")

plt.xlabel("Flexibility (less flexible → more flexible)")
plt.ylabel("Error / quantity (arbitrary units)")
plt.title("Typical Bias-Variance Tradeoff Curves")
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(bottom=0)
plt.show()
