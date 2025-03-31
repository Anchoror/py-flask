from flask import render_template, jsonify, request
from app.main import bp
from app.models import User, db


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html", title="Home")
