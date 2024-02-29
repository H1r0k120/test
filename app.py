from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Read data from Excel file (adjust the file path accordingly)
    excel_file_path = 'files/test.xlsx'
    df = pd.read_excel(excel_file_path)

    # Convert the DataFrame to a list of dictionaries for easy rendering in HTML
    data = df.to_dict(orient='records')

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
