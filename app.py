from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask_cors import CORS
from flask_login import LoginManager, login_user, logout_user, current_user
from forms import LoginForm, AddProductForm
from models import db, User, Product
from admin import admin

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMT_TRACK_MODIFICATIONS"] = False
app.config["UPLOADS_FOLDER"] = "uploads"
app.secret_key = "asdfghjkl1b0i2t9c3h84756"

login_manager = LoginManager(app)
login_manager.login_view = "login"

admin.init_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/")
def home():
    products = Product.query.all()
    return render_template("index.html", user=current_user, products=products)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(name=name, username=username, password=password).first()
        if not user:
            user = User(name=name, username=username, password=password)
            db.session.add(user)
            db.session.commit()
        login_user(user)
        return redirect(url_for("home"))
    return render_template("login.html", form=form)

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        image = form.image.data
        name = form.name.data
        product = Product.query.filter_by(name=name).first()
        if not product:
            product = Product(name=name, image=image.filename, price=form.price.data, short_description=form.short_description.data)
            image.save(f"uploads/{image.filename}")
            db.session.add(product)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_product.html", form=form)

@app.route("/uploads/images/<image>")
def get_image(image):
    return send_from_directory("uploads", image)

@app.route("/product/<product_id>")
def send_product(product_id):
    product = Product.query.get(product_id)
    return render_template("product.html", product=product)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


if __name__=='__main__':
    app.run(debug=True)
