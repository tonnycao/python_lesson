import os
from flask import Flask, escape, url_for, request, session, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import time
import pprint

from app import app, db
from models import City, Company, Employee

@app.route('/hi')
def hello_world():
    return 'Hello, World!'


@app.route('/')
def index():
    if not session['username']:
        return redirect(url_for('login'))
    return render_template('index.html', current_user={'username': session['username']})


@app.route('/table')
def table():
    page = request.args.get('page', 1, type=int)
    pagination = City.query.order_by(City.id.desc()).paginate(page, per_page=app.config['ARTISAN_POSTS_PER_PAGE'],
                                                              error_out=False)
    cc = pagination.items


    return render_template('table.html',
                           current_user={
                               'username': session['username'],
                               'city': cc,
                               'pagination': pagination,
                               'endpoint': 'table'}
                           )


@app.route('/logout')
def logout():
    del session['username']
    del session['password']
    return redirect(url_for('login'))


@app.route('/login', methods=['GET'])
def get_login():

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def post_login():
    session['username'] = request.form['username']
    session['password'] = request.form['pass']
    return redirect(url_for('index'))


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
