from flask import Blueprint, render_template
import psycopg2

bp = Blueprint("main", __name__, url_prefix="/")

CONNECTION_PARAMETERS = {
    "dbname": "calendar_this_dev",
    "user": "calendar_this",
    "password": "Ku9rSyXD"
}

@bp.route("/")
def main():
    # return render_template("main.html", title='Flask App Project')
