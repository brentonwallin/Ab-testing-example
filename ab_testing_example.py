#ab testing example
import random
import scipy.stats as stats

# Simulate user clicks for two banner versions
def simulate_clicks(banner_a_rate, banner_b_rate, num_users=1000):
    clicks_a = sum(1 for _ in range(num_users) if random.random() < banner_a_rate)
    clicks_b = sum(1 for _ in range(num_users) if random.random() < banner_b_rate)
    return clicks_a, clicks_b

# Perform A/B test using a z-test
def perform_ab_test(clicks_a, clicks_b, num_users=1000):
    rate_a = clicks_a / num_users
    rate_b = clicks_b / num_users
    
    pooled_variance = rate_a * (1 - rate_a) / num_users + rate_b * (1 - rate_b) / num_users
    z_score = (rate_a - rate_b) / pooled_variance**0.5
    p_value = 2 * stats.norm.cdf(-abs(z_score)) # Two-tailed test
    
    return z_score, p_value

# Set conversion rates for banner A and B
banner_a_rate = 0.10
banner_b_rate = 0.12

# Simulate clicks
clicks_a, clicks_b = simulate_clicks(banner_a_rate, banner_b_rate)

# Perform A/B test
z_score, p_value = perform_ab_test(clicks_a, clicks_b)

# Output results
print(f"Banner A Clicks: {clicks_a}")
print(f"Banner B Clicks: {clicks_b}")
print(f"Z-score: {z_score:.2f}")
print(f"P-value: {p_value:.3f}")

# Check for statistical significance (alpha = 0.05)
alpha = 0.05
if p_value < alpha:
    print("Result is statistically significant. Reject the null hypothesis.")
    if clicks_a > clicks_b:
        print("Banner A performs better.")
    else:
        print("Banner B performs better.")
else:
    print("Result is not statistically significant. Fail to reject the null hypothesis.")