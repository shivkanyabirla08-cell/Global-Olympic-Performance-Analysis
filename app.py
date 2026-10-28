from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Global Olympic Sports Performance Analysis</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                background: #f0f4f8;
                color: #243447;
            }
            header {
                background: #12345a;
                color: white;
                text-align: center;
                padding: 30px 15px;
            }
            main {
                max-width: 1100px;
                margin: auto;
                padding: 20px;
            }
            section {
                background: white;
                padding: 22px;
                margin: 20px 0;
                border-radius: 12px;
                box-shadow: 0 2px 8px #ccd3dc;
            }
            h2 { color: #12345a; }
            img {
                width: 100%;
                height: auto;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Global Olympic Sports Performance Analysis</h1>
            <p>Tableau Data Analytics Project</p>
        </header>
        <main>
            <section>
                <h2>About the Project</h2>
                <p>This project analyzes Olympic medals, countries,
                athletes, sports categories and performance trends.</p>
            </section>

            <section>
                <h2>Project Objectives</h2>
                <ul>
                    <li>Analyze gold, silver and bronze medals.</li>
                    <li>Compare country performance.</li>
                    <li>Explore Olympic sports and athletes.</li>
                    <li>Present insights using Tableau visualizations.</li>
                </ul>
            </section>

            <section>
                <h2>Tableau Dashboard</h2>
                <img src="https://raw.githubusercontent.com/shivkanyabirla08-cell/Global-Olympic-Performance-Analysis/main/Dashboard.png"
                     alt="Olympic Tableau Dashboard">
            </section>

            <section>
                <h2>Tableau Story</h2>
                <img src="https://raw.githubusercontent.com/shivkanyabirla08-cell/Global-Olympic-Performance-Analysis/main/Story.png"
                     alt="Olympic Tableau Story">
            </section>
        </main>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
