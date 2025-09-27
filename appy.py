from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import json, csv, os

app = Flask(__name__)
app.secret_key = "clave_secreta"   # Necesario para sesiones

# -------------------- Configuración MySQL en la nube (db4free.net) --------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario_flask:tu_contraseña@db4free.net:3306/desarrollo_web'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------- Flask-Login --------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# -------------------- Modelo MySQL --------------------
class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    mail = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))  # nueva columna para password

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Crear tablas automáticamente
with app.app_context():
    db.create_all()

# -------------------- Rutas públicas --------------------
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

# -------------------- Rutas de Registro/Login --------------------
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form['nombre']
        email = request.form['mail']
        password = generate_password_hash(request.form['password'])

        usuario_existente = Usuario.query.filter_by(mail=email).first()
        if usuario_existente:
            flash("El correo ya está registrado")
            return redirect(url_for("register"))

        nuevo = Usuario(nombre=nombre, mail=email, password=password)
        db.session.add(nuevo)
        db.session.commit()
        flash("Registro exitoso, ahora inicia sesión.")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['mail']
        password = request.form['password']
        usuario = Usuario.query.filter_by(mail=email).first()

        if usuario and check_password_hash(usuario.password, password):
            login_user(usuario)
            return redirect(url_for("protegida"))
        else:
            flash("Correo o contraseña incorrectos.")
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada.")
    return redirect(url_for("login"))

@app.route('/protegida')
@login_required
def protegida():
    return f"Bienvenido {current_user.nombre}, accediste a la ruta protegida 🎉"

# -------------------- Persistencia TXT/JSON/CSV/MySQL (igual que tu código) --------------------
# ... aquí puedes dejar las funciones guardar_txt, leer_txt, guardar_json, leer_json, etc.
