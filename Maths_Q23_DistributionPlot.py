import numpy as np
import matplotlib.pyplot as plt  # Ensure this is installed
import math

# Given parameters
lambda_param = 1 / 18  # Rate parameter
t = 15  # Time in months

# Part 1: Probability that shoes last more than 15 months
probability_more_than_15 = np.exp(-lambda_param * t)
print(f"P(X > 15 months) = {probability_more_than_15:.4f}")

# Part 2: Average lifespan of six pairs of running shoes
average_lifespan_six_pairs = 6 * 18
print(f"Average lifespan of six pairs = {average_lifespan_six_pairs:.2f} months")

# Part 3: Maximum lifespan for 80% of running shoes
percentile_80 = -np.log(0.2) * 18
print(f"80% of running shoes last at most: {percentile_80:.2f} months")

# Part 4: Plotting the exponential distribution
x = np.linspace(0, 60, 100)  # Time range in months
y = lambda_param * np.exp(-lambda_param * x)  # PDF

# Plotting the exponential distribution
plt.plot(x, y, label='Exponential Distribution', color='blue')
plt.title('Exponential Distribution of Running Shoe Lifespan')
plt.xlabel('Months')
plt.ylabel('Probability Density')
plt.axvline(x=15, color='red', linestyle='--', label='15 Months')
plt.axvline(x=percentile_80, color='green', linestyle='--', label='80% Cutoff')
plt.legend()
plt.grid()
plt.show()
