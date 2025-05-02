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

# Esto lo sumé despues
postgresql://portgresnombre_user:tu_password@dpg-d0ad57h5pdvs73cllvt0-a:5432/portgresnombre 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definición del modelo
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.before_first_request
def crear_tablas():
    db.create_all()

@app.route('/')
def index():
    return "¡App conectada y tabla creada si no existía!"

if __name__ == '__main__':
    app.run(debug=True)
