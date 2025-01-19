from scipy.stats import binom

n = 20
p = 0.41
k = 12

# Calculate P(X <= 12)
probability = binom.cdf(k, n, p)
print(probability)
