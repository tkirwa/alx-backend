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
    """Determine the best match with our supported languages"""
    return (
        g.user.get("locale")
        if g.user
        else request.accept_languages.best_match(app.config["LANGUAGES"])
    )


@app.route("/")
def index():
    """Index page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
