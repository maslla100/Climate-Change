import pandas as pd
import hvplot.pandas  # Import hvplot for pandas integration
from sqlalchemy.orm import Session
from src.db.database import engine
from src.db.models import GlobalMonthly, NorthernHemisphere, SouthernHemisphere

# Query data from the database
with Session(engine) as session:
    global_monthly = session.query(GlobalMonthly).all()
    northern_hemisphere = session.query(NorthernHemisphere).all()
    southern_hemisphere = session.query(SouthernHemisphere).all()

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

# Visualization 1: Global Temperature Anomalies Over Time
global_temp_plot = global_monthly_df.hvplot.line(x='Year', y='J-D', title="Global Temperature Anomaly Over Time")
hvplot.save(global_temp_plot, '../src/app/static/global_temperature_anomaly.html')

# Visualization 2: Average Monthly Temperature Anomalies (Jan-Dec)
monthly_anomalies = global_monthly_df[[
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]].mean()

monthly_plot = monthly_anomalies.hvplot.bar(title="Average Monthly Temperature Anomalies", ylabel="Temperature Anomaly (°C)")
hvplot.save(monthly_plot, '../src/app/static/monthly_anomalies.html')

# Visualization 3: Comparing Northern and Southern Hemisphere Anomalies
hemisphere_comparison_plot = northern_hemisphere_df.hvplot.line(x='Year', y='J-D', label='Northern Hemisphere') * \
    southern_hemisphere_df.hvplot.line(x='Year', y='J-D', color='orange', label='Southern Hemisphere', title="Northern vs Southern Hemisphere Temperature Anomalies")
hvplot.save(hemisphere_comparison_plot, '../src/app/static/hemisphere_anomalies_comparison.html')

# Visualization 4: Seasonal Temperature Anomalies Over Time (DJF, MAM, JJA, SON)
seasonal_plot = global_monthly_df.hvplot.line(x='Year', y=['DJF', 'MAM', 'JJA', 'SON'], title="Seasonal Temperature Anomalies Over Time")
hvplot.save(seasonal_plot, '../src/app/static/seasonal_anomalies.html')

# Visualization 5: Heatmap of Monthly Temperature Anomalies Over Time
monthly_anomalies_df = global_monthly_df.set_index('Year')[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
heatmap_plot = monthly_anomalies_df.hvplot.heatmap(cmap='coolwarm', title="Heatmap of Monthly Temperature Anomalies Over Time")
hvplot.save(heatmap_plot, '../src/app/static/monthly_anomalies_heatmap.html')
