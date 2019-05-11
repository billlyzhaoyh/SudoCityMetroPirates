from flask import Flask
from flask import render_template
from flask import request

import json

app = Flask(__name__)

@app.route('/')
def homepage():
     return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

   if request.form.get('start') is not None and request.form.get('end') is not None :



        return json.dumps({'test': 'xxx'})
   else :
        return 'FAIL'

