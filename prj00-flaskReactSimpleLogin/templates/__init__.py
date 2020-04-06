from pathlib import Path, PurePath
from flask import Flask

BASE_DIR = Path(__file__).parent.resolve()

PUB_DIR = PurePath(BASE_DIR / 'public')
STAT_DIR = PurePath(BASE_DIR / 'static')

# print(PUB_DIR, PurePath(BASE_DIR / 'public'), sep=' | ')

app = Flask(__name__, static_folder= PUB_DIR, template_folder= STAT_DIR)

from templates.hello.views import hello_blueprint

# register de blueprints
app.register_blueprint(hello_blueprint)
