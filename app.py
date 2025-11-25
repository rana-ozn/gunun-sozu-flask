from flask import Flask, render_template
import random

app = Flask(__name__)

# Dictionary yapısında günün verileri
sozler = [
    {"baslik": "Open Resource Portal", "link": "openresource.net"},
    {"baslik": "Python Docs", "link": "https://docs.python.org"},
    {"baslik": "Flask Tutorial", "link": "https://flask.palletsprojects.com"},
    {"baslik": "W3Schools", "link": "https://w3schools.com"},
    {"baslik": "Stack Overflow", "link": "https://stackoverflow.com"}
]

@app.route('/')
def index():
    bugunku_soz = random.choice(sozler)  # Rastgele seç
    return render_template('index.html', soz=bugunku_soz)

if __name__ == "__main__":
    app.run(debug=True)
