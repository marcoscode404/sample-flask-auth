from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key" ## onde o banco de dados vai ficar
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' ## caminho para o banco

db = SQLAlchemy(app)

@app.route("/hello-world", methods=["GET"])
def hello_word():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)