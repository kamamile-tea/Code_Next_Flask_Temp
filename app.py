from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)

 
# -- Routes section -- 

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', time=datetime.now())
