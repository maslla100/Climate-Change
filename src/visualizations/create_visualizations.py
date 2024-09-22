import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
global_monthly = pd.read_csv('../data/cleaned/cleaned_globalmonthlyandseasonal.csv')

# Example: Generate a plot and save it
plt.plot(global_monthly['Year'], global_monthly['J-D'])
plt.title("Global Temperature Anomaly Over Time")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.savefig('../docs/global_temperature_anomaly.png')
