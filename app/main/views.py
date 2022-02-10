from flask import Flask, render_template
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload_form.html')

@main.route('/learn', methods=['GET'])
def learn():
    return render_template('learn.html')

@main.route('/research', methods=['GET'])
def research():
    return render_template('research.html')