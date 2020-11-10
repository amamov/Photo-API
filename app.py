from flask import Flask, render_template
from flask_cors import CORS

app = Flask(
    __name__,
    static_url_path="",
    static_folder="build/static",
    template_folder="build/templates",
)
cors = CORS(app, resources={r"*": {"origin": "*"}})

from api_v1 import api as api_v1
from views import view

app.register_blueprint(api_v1, url_prefix="/api/v1")
app.register_blueprint(view, url_prefix="/")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
