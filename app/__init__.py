import numpy as np
from datetime import datetime

from flask import Flask

app = Flask(__name__)

# Setup the app with the config.py file
app.config.from_object('app.config.default')
app.config.from_envvar("APP_CONFIG_FILE")

mysql_username = app.config["MYSQL_USERNAME"]
mysql_password = app.config["MYSQL_PASSWORD"]
mysql_host = app.config["MYSQL_HOST"]
mysql_port = app.config["MYSQL_PORT"]
mysql_db = app.config["MYSQL_DB"]

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"

# Setup the database
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
db.init_app(app)

# Setup the debug toolbar
from flask_debugtoolbar import DebugToolbarExtension

app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

# Setup the password crypting
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Import the views
from app.views import user, main, context_processors

app.register_blueprint(user.userbp)
app.register_blueprint(main.mainbp)

# Setup the user login process
from flask_login import LoginManager
from app.models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'userbp.signin'


@login_manager.user_loader
def load_user(email):
    return User.query.filter(User.email == email).first()


@app.context_processor
def utility_processor():
    def get_interval(value, log_interval_width):
        if value:
            log_value = np.log10(value)
            log_low, log_high = log_value - log_interval_width, log_value + log_interval_width
            low, high = 10 ** log_low, 10 ** log_high
            return int(low), int(high)
        else:
            return '', ''

    def lowercase(s):
        if s:
            return s.lower()
        else:
            return ''

    def parse_number(number, n_decimals=0):
        if number:
            if n_decimals > 0:
                return f'{round(number, n_decimals):,}'
            elif n_decimals == 0:
                return f'{round(number):,}'
            else:
                return ''
        else:
            return ''

    def parse_seconds(number):
        if number:
            return str(datetime.timedelta(seconds=666))
        else:
            return ''

    def split_products(products, n_splits):
        n_products_per_splits = len(products) // n_splits
        if n_products_per_splits > 0:
            data = [products[i * n_products_per_splits: (i + 1) * n_products_per_splits] if i != n_splits else products[i * n_products_per_splits:]
                    for i in range(n_splits)]
        else:
            data = [[p] for p in products]
        return data

    def parse_date(date):
        return date.year, str(date.month).zfill(2), str(date.day).zfill(2)

    def get_screenshot_path(store_url):
        assert isinstance(store_url, str)
        return f'{app.config.get("STORE_SCREENSHOT_URI")}/{store_url}.png'

    return dict(get_interval=get_interval, lowercase=lowercase, parse_number=parse_number,
                parse_seconds=parse_seconds, split_products=split_products, parse_date=parse_date,
                get_screenshot_path=get_screenshot_path)