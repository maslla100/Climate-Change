import os
import sys

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from flask import Flask, render_template
from sqlalchemy.orm import Session
from src.db.database import engine  # Changed relative import to absolute import
from src.db.models import GlobalMonthly, NorthernHemisphere, SouthernHemisphere  # Changed relative import to absolute import
import pandas as pd
import hvplot.pandas
import holoviews as hv
from bokeh.embed import components  # Import Bokeh components for embedding

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualize')
def visualize():
    # Start the session
    session = Session(engine)
    try:
        # Query the GlobalMonthly, NorthernHemisphere, and SouthernHemisphere tables from the database
        global_monthly = session.query(GlobalMonthly).all()
        northern_hemisphere = session.query(NorthernHemisphere).all()
        southern_hemisphere = session.query(SouthernHemisphere).all()
        
        # Convert the query results to pandas DataFrames for easy plotting
        global_monthly_df = pd.DataFrame([{
            'Year': row.year, 'J-D': row.j_d
        } for row in global_monthly])

        northern_hemisphere_df = pd.DataFrame([{
            'Year': row.year, 'J-D': row.j_d
        } for row in northern_hemisphere])

        southern_hemisphere_df = pd.DataFrame([{
            'Year': row.year, 'J-D': row.j_d
        } for row in southern_hemisphere])

        # Example: Create hvPlot for Global Temperature Anomalies
        global_temp_plot = global_monthly_df.hvplot.line(x='Year', y='J-D', title="Global Temperature Anomalies Over Time")
        
        # Convert the hvPlot (Holoviews) plot to Bokeh components (script and div)
        plot = hv.render(global_temp_plot, backend='bokeh')
        plot_script, plot_div = components(plot)  # Embed Bokeh plot in Flask template

        # Render the template with the plot's script and div
        return render_template('visualization.html', plot_script=plot_script, plot_div=plot_div)

    finally:
        # Always close the session to prevent database connection leaks
        session.close()

if __name__ == '__main__':
    app.run(debug=True)
