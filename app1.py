import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

app = Flask(__name__)

# Leer las variables de entorno
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

# Configurar la URI de PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Modelo de ejemplo
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)

# Crear las tablas si no existen y crear un usuario de prueba
with app.app_context():
    db.create_all()

    # Verificar si el usuario de prueba ya existe
    if not Usuario.query.filter_by(correo='prueba@example.com').first():
        usuario_prueba = Usuario(nombre='Usuario Prueba', correo='prueba@example.com')
        db.session.add(usuario_prueba)
        db.session.commit()
        print("✅ Usuario de prueba creado.")
    else:
        print("ℹ️ Usuario de prueba ya existe.")

# Ruta principal
@app.route('/')
def home():
    return render_template('ingreso.html')

# Ruta para ver los usuarios registrados
@app.route('/usuarios')
def listar_usuarios():
    print("➡ Se accedió a la ruta /usuarios")
    usuarios = Usuario.query.all()
    return '<br>'.join([f'{u.id} - {u.nombre} - {u.correo}' for u in usuarios])

# Ejecutar localmente
if __name__ == '__main__':
    app.run(debug=True)
