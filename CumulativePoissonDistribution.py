from scipy.stats import poisson

# Parameters
lambda_param = 32  # Average rate (lambda) for 8 minutes
k = 40  # Number of occurrences

# Calculate cumulative probability P(X ≤ 40)
cumulative_prob = poisson.cdf(k, lambda_param)

# Print the result
print(f"P(X ≤ {k}) = {cumulative_prob:.4f}")
