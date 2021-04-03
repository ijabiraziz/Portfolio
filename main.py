from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'

app.config['SECRET_KEY'] = 'thisisaveryverysecret'
db = SQLAlchemy(app)


class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    message = db.Column(db.String(200), nullable=False)


@app.route('/')
@app.route("/home")
def home():
    return render_template("main.html")


@app.route('/', methods=['POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form["name"]
            email = request.form["email"]
            message = request.form["message"]

            entry = Contacts(name=name, email=email, message=message)

            db.session.add(entry)
            db.session.commit()
            return render_template('/')
        except:
            return redirect('/')

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=False)
