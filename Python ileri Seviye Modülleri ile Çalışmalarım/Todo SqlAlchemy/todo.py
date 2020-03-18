from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Mustafa/Desktop/sync/Todo/todo.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


