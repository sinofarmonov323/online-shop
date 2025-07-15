from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, FileField


class LoginForm(FlaskForm):
    name = StringField("Name", validators=[validators.DataRequired()])
    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
    submit = SubmitField("login")

class AddProductForm(FlaskForm):
    image = FileField("Upload Image", validators=[validators.DataRequired(message="you need to upload an image")])
    name = StringField("Enter name", validators=[validators.DataRequired(message="you need to enter a name")])
    price = StringField("Enter price", validators=[validators.DataRequired(message="you need to enter a price")])
    short_description = StringField("Enter short description", validators=[validators.DataRequired(message="you need to enter a short description")])
    submit = SubmitField("Add", validators=[validators.DataRequired(message="you have to submit")])
