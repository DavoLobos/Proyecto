from flask import Blueprint, render_template, redirect, url_for, flash
from forms.registro_form import RegistroForm
from models.usuario import db, Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        existente = Usuario.query.filter_by(correo=form.correo.data).first()
        if existente:
            flash('El correo ya está registrado.')
        else:
            nuevo_usuario = Usuario(nombre=form.nombre.data, correo=form.correo.data)
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('¡Registro exitoso!')
            return redirect(url_for('auth.registro'))
    return render_template('registro.html', form=form)
