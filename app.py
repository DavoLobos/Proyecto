from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ingreso.html')

# Este if es útil para correr localmente, pero Render usará gunicorn
if __name__ == '__main__':
    app.run(debug=True)


# Esto es para ver si nos podemos conectar a la base de datos
import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
