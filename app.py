
from flask import Flask, render_template
from config import Config
from models.usuario import db, Usuario
from routes.auth_routes import auth_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('ingreso.html')

@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return '<br>'.join([f'{u.id} - {u.nombre} - {u.correo}' for u in usuarios])

if __name__ == '__main__':
    app.run(debug=True)
