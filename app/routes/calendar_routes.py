from flask import Blueprint, render_template
import psycopg2
import os

bp = Blueprint("main", __name__, url_prefix="/appointments")

CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}

# CONNECTION_PARAMETERS = {
#     "user": "calendar_this",
#     "password": "K",
#     "dbname": os.environ.get("DB_NAME"),
#     "host": os.environ.get("DB_HOST"),
# }

@bp.route("/")
def main():
    # return "we got to appointments get route"
    with psycopg2.connect(**CONNECTION_PARAMETERS) as banana:
        with banana.cursor() as curs: 
            curs.execute(
                """
                SELECT id, name, start_datetime, end_datetime FROM
                appointments
                ORDER BY start_datetime;
                """
            )
            
            rows = curs.fetchall()
            print(rows)
            
            if rows:
                return render_template("main.html", title='Flask App Project', rows=rows )
            else:
                return "oops"
            
            