from flask import Blueprint, render_template
import psycopg2

bp = Blueprint("main", __name__, url_prefix="/")

CONNECTION_PARAMETERS = {
    "dbname": "calendar_this_dev",
    "user": "calendar_this",
    "password": "password"
}

@bp.route("/")
def main():
    # return render_template("main.html", title='Flask App Project') 

    with psycopg2.connect(**CONNECTION_PARAMETERS) as banana:
        with banana.cursor() as curs:
            def create_table():
                curs.execute(
                    """
                    CREATE TABLE calendar (
                    id SERIAL PRIMARY KEY,
                    day VARCHAR(50),
                    fieldone VARCHAR(50)
                    )
                    """
                )