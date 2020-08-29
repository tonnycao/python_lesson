from functools import wraps
from datetime import datetime
from flask import flash, redirect, url_for
from werkzeug.routing import BaseConverter
from flask_login import current_user


class ListConverter(BaseConverter):

    def to_python(self, value):
        return value.split('+')

    def to_url(self, values):
        return '+'.join(BaseConverter.to_url(value)
                        for value in values)


def check_expired(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if datetime.utcnow() > current_user.account_expires:
            flash("Your account has expired. Update your billing info.")
            return redirect(url_for('account_billing'))
        return func(*args, **kwargs)

    return decorated_function

