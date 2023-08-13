from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, Form, BooleanField
from wtforms.validators import DataRequired, Email, Length, InputRequired
from email_validator import validate_email, EmailNotValidError
from flask_bootstrap import Bootstrap4


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[Email(message='not a valid email address')])
    password = PasswordField(label="Password", validators=[Length(min=6, message='Not long enough')])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
bootstrap = Bootstrap4(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            print("1")
            return render_template('success.html')
        else:
            print("2")
            return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
