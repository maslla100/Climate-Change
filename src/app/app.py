from flask import Flask, render_template
from src.db.database import get_db
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualize')
def visualize():
    # Load cleaned data and generate visualizations dynamically
    global_monthly = pd.read_csv('../data/cleaned/cleaned_globalmonthlyandseasonal.csv')
    # (Insert code for visualizations here)
    return render_template('visualization.html')

if __name__ == '__main__':
    app.run(debug=True)
