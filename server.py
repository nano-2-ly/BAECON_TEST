from flask import Flask, render_template, request,redirect,jsonify
import requests
import json 
from random import randint
import os
# from flask_bootstrap import Bootstrap
app = Flask(__name__)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.get_data()
    print(text)
    return text

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8080")