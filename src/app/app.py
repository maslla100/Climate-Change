from flask import Flask, render_template
from sqlalchemy.orm import Session
from src.db.database import engine
from src.db.models import GlobalMonthly, NorthernHemisphere, SouthernHemisphere
import pandas as pd
import hvplot.pandas

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

        # Example: Create hvPlot for Global Temperature Anomalies and save to HTML
        global_temp_plot = global_monthly_df.hvplot.line(x='Year', y='J-D', title="Global Temperature Anomalies Over Time")
        global_temp_html = global_temp_plot.to_html()

        # Render the template with the HTML interactive plots
        return render_template('visualization.html', global_temp_html=global_temp_html)

    finally:
        # Always close the session to prevent database connection leaks
        session.close()

if __name__ == '__main__':
    app.run(debug=True)
