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

@main.route('/overview',methods=['GET'])
def overview():
    return render_template('overview.html')

@main.route('/people',methods=['GET'])
def people():
    return render_template('people.html') 

@main.route('/resource',methods=['GET'])
def resource():
    return render_template('resource.html') 

@main.route('/workshops',methods=['GET'])
def workshops():
    return render_template('workshops.html')

@main.route('/program',methods=['GET'])
def program():
    return render_template('programs.html')

@main.route('/signup',methods=['GET']) 
def signup():
    return render_template('signup.html')
    
@main.route('/login',methods=['GET']) 
def login():
    return render_template('login.html')

@main.route('/deposit',methods=['GET','POST']) 
def deposit():
    return render_template('deposit.html')