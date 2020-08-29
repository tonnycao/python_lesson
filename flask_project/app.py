from __future__ import unicode_literals
import config

from flask import (Flask, render_template, redirect, url_for, request, flash, g)
from flask_bootstrap import Bootstrap
from flask_login import login_required, login_user, logout_user, current_user, LoginManager

from forms import LoginForm
from models import CsvTable, User, db

SECRET_KEY = 'This is my key'

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS


db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@app.route('/index', methods=['GET'])
@login_required
def show_csv_list():
    page = request.args.get('page', 1, type=int)
    csvlists_pagination = CsvTable.query.order_by(CsvTable.cust_id.desc()).paginate(
        page,per_page=50,
        error_out=False
    )
    csvlist = csvlists_pagination.items
    return render_template('index.html', csvlists=csvlist, pagination = csvlists_pagination)


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user:
            login_user(user)
            flash('you have logged in!')
            return redirect(url_for('show_csv_list'))
        else:
            flash('Invalid username or password')
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have logout!')
    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
