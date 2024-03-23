from flask import Flask
from endpoints import api
from db.models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['ERROR_404_HELP'] = False

api.init_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=80)
