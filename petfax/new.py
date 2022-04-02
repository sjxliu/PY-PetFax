from flask import (Blueprint, render_template)
import json

bp = Blueprint("add", __name__, url_prefix="/fact")

bp.route("/new")
def new_fact():
    return render_template("add_new.html")