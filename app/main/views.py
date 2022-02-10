from flask import Flask, render_template
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/upload')
def upload():
    return render_template('upload_form.html')

@main.route('/learn')
def learn():
    return render_template('learn.html')

@main.route('/research')
def research():
    return render_template('research.html')