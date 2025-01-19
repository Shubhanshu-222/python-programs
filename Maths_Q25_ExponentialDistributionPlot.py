import numpy as np
import matplotlib.pyplot as plt  # Ensure this is installed

# Given parameters
lambda_param = 0.5  # Rate parameter (30 customers per hour = 0.5 customers per minute)

# Part a: Average time between arrivals
average_time_between_arrivals = 1 / lambda_param
print(f"Average time between two successive arrivals: {average_time_between_arrivals:.2f} minutes")

# Part b: Time taken for three customers to arrive
time_for_three_customers = 3 / lambda_param
print(f"Average time for three customers to arrive: {time_for_three_customers:.2f} minutes")

# Part c: Probability that it takes less than one minute for the next customer
t_c = 1  # Time in minutes
probability_less_than_1 = 1 - np.exp(-lambda_param * t_c)
print(f"P(T < 1 minute) = {probability_less_than_1:.4f}")

# Part d: Probability that it takes more than five minutes for the next customer
t_d = 5  # Time in minutes
probability_more_than_5 = np.exp(-lambda_param * t_d)
print(f"P(T > 5 minutes) = {probability_more_than_5:.4f}")

# Part e: Time within which 70% of customers arrive
percentile_70 = -np.log(0.3) / lambda_param
print(f"70% of customers arrive within {percentile_70:.2f} minutes")

# Part f: Plotting the exponential distribution
x = np.linspace(0, 10, 100)  # Time range in minutes
y = lambda_param * np.exp(-lambda_param * x)  # PDF

# Plotting the exponential distribution
plt.plot(x, y, label='Exponential Distribution', color='blue')
plt.title('Exponential Distribution of Customer Arrivals')
plt.xlabel('Time (minutes)')
plt.ylabel('Probability Density')
plt.axvline(x=1, color='red', linestyle='--', label='1 Minute Cutoff')
plt.axvline(x=5, color='green', linestyle='--', label='5 Minutes Cutoff')
plt.axvline(x=percentile_70, color='purple', linestyle='--', label='70% Cutoff')
plt.legend()
plt.grid()
plt.show()
