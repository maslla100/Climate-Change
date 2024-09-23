import sys
import os
import pandas as pd
import hvplot.pandas  # Import hvplot for pandas integration
from sqlalchemy.orm import Session

# Add the project root to sys.path before importing from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import the engine and models after adding to sys.path
from src.db.database import engine
from src.db.models import GlobalMonthly, NorthernHemisphere, SouthernHemisphere

# Print out the sys.path for debugging
print("Current sys.path:", sys.path)

# Ensure the output directory exists
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/app/static/'))
os.makedirs(output_dir, exist_ok=True)

# Query data from the database
try:
    with Session(engine) as session:
        global_monthly = session.query(GlobalMonthly).all()
        northern_hemisphere = session.query(NorthernHemisphere).all()
        southern_hemisphere = session.query(SouthernHemisphere).all()
except Exception as e:
    print(f"Error querying the database: {e}")
    sys.exit(1)

# Convert query results to DataFrames
global_monthly_df = pd.DataFrame([{
    'Year': row.year, 'Jan': row.jan, 'Feb': row.feb, 'Mar': row.mar, 'Apr': row.apr,
    'May': row.may, 'Jun': row.jun, 'Jul': row.jul, 'Aug': row.aug, 'Sep': row.sep,
    'Oct': row.oct, 'Nov': row.nov, 'Dec': row.dec, 'J-D': row.j_d, 'D-N': row.d_n,
    'DJF': row.djf, 'MAM': row.mam, 'JJA': row.jja, 'SON': row.son
} for row in global_monthly])

northern_hemisphere_df = pd.DataFrame([{
    'Year': row.year, 'J-D': row.j_d
} for row in northern_hemisphere])

southern_hemisphere_df = pd.DataFrame([{
    'Year': row.year, 'J-D': row.j_d
} for row in southern_hemisphere])

# Check if dataframes have data
if global_monthly_df.empty or northern_hemisphere_df.empty or southern_hemisphere_df.empty:
    print("Error: Some queried data is empty. Please check the database.")
    sys.exit(1)

# Visualization 1: Global Temperature Anomalies Over Time
try:
    global_temp_plot = global_monthly_df.hvplot.line(x='Year', y='J-D', title="Global Temperature Anomaly Over Time")
    hvplot.save(global_temp_plot, os.path.join(output_dir, 'global_temperature_anomaly.html'))
except Exception as e:
    print(f"Error saving global temperature anomaly plot: {e}")

# Visualization 2: Average Monthly Temperature Anomalies (Jan-Dec)
try:
    monthly_anomalies = global_monthly_df[[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]].mean()

    monthly_plot = monthly_anomalies.hvplot.bar(title="Average Monthly Temperature Anomalies", ylabel="Temperature Anomaly (°C)")
    hvplot.save(monthly_plot, os.path.join(output_dir, 'monthly_anomalies.html'))
except Exception as e:
    print(f"Error saving monthly anomalies plot: {e}")

# Visualization 3: Comparing Northern and Southern Hemisphere Anomalies
try:
    hemisphere_comparison_plot = northern_hemisphere_df.hvplot.line(x='Year', y='J-D', label='Northern Hemisphere') * \
        southern_hemisphere_df.hvplot.line(x='Year', y='J-D', color='orange', label='Southern Hemisphere', title="Northern vs Southern Hemisphere Temperature Anomalies")
    hvplot.save(hemisphere_comparison_plot, os.path.join(output_dir, 'hemisphere_anomalies_comparison.html'))
except Exception as e:
    print(f"Error saving hemisphere comparison plot: {e}")

# Visualization 4: Seasonal Temperature Anomalies Over Time (DJF, MAM, JJA, SON)
try:
    seasonal_plot = global_monthly_df.hvplot.line(x='Year', y=['DJF', 'MAM', 'JJA', 'SON'], title="Seasonal Temperature Anomalies Over Time")
    hvplot.save(seasonal_plot, os.path.join(output_dir, 'seasonal_anomalies.html'))
except Exception as e:
    print(f"Error saving seasonal anomalies plot: {e}")

# Visualization 5: Heatmap of Monthly Temperature Anomalies Over Time
try:
    monthly_anomalies_df = global_monthly_df.set_index('Year')[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
    heatmap_plot = monthly_anomalies_df.hvplot.heatmap(cmap='coolwarm', title="Heatmap of Monthly Temperature Anomalies Over Time")
    hvplot.save(heatmap_plot, os.path.join(output_dir, 'monthly_anomalies_heatmap.html'))
except Exception as e:
    print(f"Error saving heatmap plot: {e}")
