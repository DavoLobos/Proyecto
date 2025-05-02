from flask import Flask, render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ingreso.html')

# Este if es útil para correr localmente, pero Render usará gunicorn
if __name__ == '__main__':
    app.run(debug=True)


