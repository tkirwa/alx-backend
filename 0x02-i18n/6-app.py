#!/usr/bin/env python3
"""
A Basic flask application
"""
from typing import (
    Dict, Union
)

from flask import Flask
from flask import g, request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
    Validate user login details
    Args:
        id (str): user id
    Returns:
        (Dict): user dictionary if id is valid else None
    """
    return users.get(int(id), {})


@babel.localeselector
@babel.localeselector
def get_locale():
    # 1. Locale from URL parameters
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    # 2. Locale from user settings
    if g.user and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config["LANGUAGES"])

    # 4. Default locale (if none of the above match)
    return app.config["BABEL_DEFAULT_LOCALE"]



@app.before_request
def before_request() -> None:
    """
    Adds valid user to the global session object `g`
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
