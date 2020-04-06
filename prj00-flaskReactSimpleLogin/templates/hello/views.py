from pathlib import Path
from flask import render_template, Blueprint

BASE_DIR = Path(__file__).parent.resolve()
print(BASE_DIR)

hello_blueprint = Blueprint('hello', __name__)

@hello_blueprint.route('/')
@hello_blueprint.route('/hello')
def index():
	return render_template("index.html")
