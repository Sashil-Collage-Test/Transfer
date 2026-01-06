import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
np.random.seed(42)
sample1 = np.random.normal(loc=10, scale=2, size=30)
sample2 = np.random.normal(loc=12, scale=2, size=30)
t_statistic, p_value = stats.ttest_ind(sample1, sample2)
alpha = 0.05
print("Results of Two-Sample t-test:")
print("T-statistic:", t_statistic)
print("P-value:", p_value)
print("Degrees of Freedom:", len(sample1) + len(sample2) - 2)
plt.figure(figsize=(10, 5))
plt.hist(sample1, alpha=0.5, label='Sample 1', color='blue')
plt.hist(sample2, alpha=0.5, label='Sample 2', color='orange')
plt.axvline(np.mean(sample1), color='blue', linestyle='dashed', linewidth=2)
plt.axvline(np.mean(sample2), color='orange', linestyle='dashed', linewidth=2)
plt.title('Distributions of Sample 1 and Sample 2')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
t_critical = stats.t.ppf(1 - alpha/2, len(sample1) + len(sample2) - 2)
sample_min, sample_max = min(sample1.min(), sample2.min()), max(sample1.max(), sample2.max())
x_vals = np.linspace(sample_min, sample_max, 100)
critical_region = np.abs(x_vals - np.mean(sample1)) > t_critical
plt.fill_between(x_vals, 0, 5, where=critical_region, alpha=0.3, label='Critical Region')
plt.text(11.5, 5, f"T = {t_statistic:.2f}", ha='center', color='black', backgroundcolor='white')
plt.show()
if p_value < alpha:
    print("\nConclusion: There is significant evidence to reject the null hypothesis.")
    print("Interpretation: The mean of Sample 1 is significantly higher than that of Sample 2.")
else:
    print("\nConclusion: Fail to reject the null hypothesis.")
    print("Interpretation: There is not enough evidence to claim a significant difference between the means.")
# chi-test
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings
from scipy import stats
warnings.filterwarnings('ignore')
df = sb.load_dataset('mpg')
print(df)
print(df['horsepower'].describe())
print(df['model_year'].describe())
# Binning horsepower
bins = [0, 75, 150, 240]
df['horsepower_new'] = pd.cut(df['horsepower'], bins=bins, labels=['l', 'm', 'h'])
print(df['horsepower_new'])
ybins = [69, 72, 74, 84]
label = ['1', '2', '3']
df['modelyear_new'] = pd.cut(df['model_year'], bins=ybins, labels=label)
newyear = df['modelyear_new']
print(newyear)
df_chi = pd.crosstab(df['horsepower_new'], df['modelyear_new'])
print(df_chi)
print(stats.chi2_contingency(df_chi))
