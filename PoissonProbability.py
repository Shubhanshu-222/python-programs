from scipy.stats import poisson

# Parameters
lambda_param = 147  # Average rate
k = 160  # Number of emails

# Calculate probability P(X = 160)
probability_exact = poisson.pmf(k, lambda_param)
print(f"P(X = {k}) = {probability_exact:.6f}")

# Calculate cumulative probability P(X ≤ 160)
probability_at_most = poisson.cdf(k, lambda_param)
print(f"P(X ≤ {k}) = {probability_at_most:.6f}")
