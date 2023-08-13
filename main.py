from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(["@", "."])])
    password = PasswordField("password", validators=[DataRequired()])


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
