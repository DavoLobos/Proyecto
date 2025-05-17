from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=50)])
    correo = StringField('Correo', validators=[DataRequired(), Email(), Length(max=120)])
    submit = SubmitField('Registrarse')

