
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Global Olympic Sports Performance Analysis</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f0f4f8;
                margin: 0;
                color: #243447;
            }
            header {
                background: #12345a;
                color: white;
                padding: 35px 20px;
                text-align: center;
            }
            main {
                max-width: 900px;
                margin: 30px auto;
                padding: 25px;
            }
            .card {
                background: white;
                padding: 25px;
                margin: 18px 0;
                border-radius: 12px;
                box-shadow: 0 2px 8px #ccd3dc;
            }
            h2 { color: #12345a; }
        </style>
    </head>
    <body>
        <header>
            <h1>Global Olympic Sports Performance Analysis</h1>
            <p>Tableau Data Analytics Project</p>
        </header>
        <main>
            <div class="card">
                <h2>About the Project</h2>
                <p>This project analyzes Olympic medals, countries,
                athletes, sports categories and performance trends.</p>
            </div>
            <div class="card">
                <h2>Project Objectives</h2>
                <ul>
                    <li>Analyze gold, silver and bronze medals.</li>
                    <li>Compare country performance.</li>
                    <li>Explore Olympic sports and athletes.</li>
                    <li>Present insights using Tableau visualizations.</li>
                </ul>
            </div>
            <div class="card">
                <h2>Tools Used</h2>
                <p>Tableau Desktop, Python and Flask.</p>
            </div>
            <div class="card">
                <h2>Tableau Dashboard</h2>
                <p>The Tableau workbook is part of this project.
                Dashboard publishing is still in progress.</p>
            </div>
        </main>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
