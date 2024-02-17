from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelos de Datos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=True, default="default.jpg")
    name = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class PostUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref="posts")

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


# Llaves primarias compuestas

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post_user.id"), nullable=False)
    user = db.relationship("User", backref="comments")
    post = db.relationship("PostUser", backref="comments")

    def __repr__(self):
        return f"Comment('{self.content}', '{self.user_id}', '{self.post_id}')"

#Creación de tablas

with app.app_context():
    db.create_all()

# Métodos http
# GET: Obtener datos
# POST: Crear datos
# PUT: Actualizar datos
# DELETE: Eliminar datos


# Declaración de rutas

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello, World!"


@app.route("/hello")
def hello():
    return "Hello, World desde otra ruta!"


@app.route("/hello_template")
def hello_template():
    lista = [
        {"num": 1, "visible": True},
        {"num": 2, "visible": False},
        {"num": 3, "visible": True},
    ]
    return render_template("ejemplo.html", nombre="Juan", lista=lista)


@app.route("/hello_template/<nombre>")
def hello_template_nombre(nombre):
    return render_template("ejemplo_parametro.html", nombre=nombre)

@app.route("/obtener_lista")
def obtener_lista():
    lista = [
        {"num": 1, "visible": True},
        {"num": 2, "visible": False},
        {"num": 3, "visible": True},
    ]
    return jsonify(lista)


@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    body = request.json
    print(body)
    if body:
        username = body["username"]
        email = body["email"]
        password = body["password"]
        name = body["name"] if "name" in body else None
        
        # Creamos el objeto user
        user = User(username=username, email=email, password=password, name=name)

        # Agregamos el objeto a la base de datos
        db.session.add(user)

        # Guardamos los cambios
        db.session.commit()

        return jsonify({"message": "Usuario creado"}), 201
    
    else:
        return jsonify({"message": "No se enviaron datos"}), 400


@app.route("/obtener_usuarios", methods=["GET"])
def obtener_usuarios():
    users = User.query.all()
    print(users)

    return jsonify([{"username": user.username, "email": user.email, "name": user.name} for user in users])



@app.route("/crear_post", methods=["POST"])
def crear_post():
    body = request.json
    print(body)
    if body:
        title = body["title"]
        content = body["content"]
        user_id = body["user_id"]

        user = User.query.get(user_id)

        if user: 
            # Creamos el objeto user
            post = PostUser(title=title, content=content, user_id=user_id)

            # Agregamos el objeto a la base de datos
            db.session.add(post)

            # Guardamos los cambios
            db.session.commit()

            return jsonify({"message": "Post creado"}), 201
        else:
            return jsonify({"message": "Usuario no existe"}), 400
    
    else:
        return jsonify({"message": "No se enviaron datos"}), 400



@app.route("/create_comment", methods=["POST"])
def create_comment():
    body = request.json
    print(body)
    if body:
        content = body["content"]
        user_id = body["user_id"]
        post_id = body["post_id"]

        user = User.query.get(user_id)
        post = PostUser.query.get(post_id)

        if user and post: 
            # Creamos el objeto user
            comment = Comment(content=content, user_id=user_id, post_id=post_id)

            # Agregamos el objeto a la base de datos
            db.session.add(comment)

            # Guardamos los cambios
            db.session.commit()

            return jsonify({"message": "Comentario creado"}), 201
        else:
            return jsonify({"message": "Usuario o post no existe"}), 400
    
    else:
        return jsonify({"message": "No se enviaron datos"}), 400


@app.route("/modificar_usuario/<int:id>", methods=["PUT"])
def modificar_usuario(id):
    body = request.json
    user = User.query.get(id)

    if user:
        for key, value in body.items():
            setattr(user, key, value)
        
        db.session.commit()
        return jsonify({"message": "Usuario modificado"}), 200
    else:
        return jsonify({"message": "Usuario no existe"}), 400



if __name__ == "__main__":
    app.run(debug=True)
