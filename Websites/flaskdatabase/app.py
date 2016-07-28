from flask import Flask, render_template, redirect, url_for, request, session
from flask.ext.sqlalchemy import SQLAlchemy

#Create app object
app = Flask(__name__)

app.secret_key = "my precious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

#create the sqlalchemy object
db = SQLAlchemy(app)
