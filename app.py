## other imports ##
from uuid import uuid4
from datetime import datetime, timezone

## flask imports ##
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

## DB setup ##
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disabling some memory intensive background workload
db = SQLAlchemy(app)

## models ##
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    share_link_id = db.Column(db.String, db.ForeignKey('share_link.id'))

class ShareLink(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    created_date = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    expiry_date = db.Column(db.DateTime, nullable=True)
    files = db.relationship('File', backref='share_link', lazy=True)

## routing ##
@app.route("/")
def index():
    return "Flask is installed :)"

## main loop ##
if __name__ == "__main__":
    # To ensure tables are created (only ones)
    with app.app_context():
        db.create_all()
    app.run()
