from flask import Flask
from endpoints import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=80)
