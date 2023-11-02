#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config(object):
    """Configuration class for Babel"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Returns a user dictionary or None"""
    try:
        return users.get(int(request.args.get("login_as")))
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Use get_user to find a user if any, and set it as a global
      on flask.g.user
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Selects the best language match from the available languages.

    The order of priority is:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale

    Returns:
        str: The best language match.
    """
    # Locale from URL parameters
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    # Locale from user settings
    user = get_user()
    if user and user["locale"] in app.config["LANGUAGES"]:
        return user["locale"]

    # Locale from request header
    return request.accept_languages.best_match(app.config["LANGUAGES"])



@app.route("/")
def index():
    """Index page"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
