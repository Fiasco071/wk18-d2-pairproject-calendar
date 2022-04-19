from flask import Flask, render_template
from app.config import Config

# print(__name__)
app = Flask(__name__)
# print(app.config)
app.config.from_object(Config)

# app.register_blueprint(books_router)

@app.route("/")
def index():
    return "hello"
    # return render_template("index.html", display_item=my_list, title="Welcome!")