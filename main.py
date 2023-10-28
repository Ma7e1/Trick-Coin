from core import *
from flask import Flask, request
import hashlib, re
app = Flask(__name__)
pattern = re.compile(r".*\.[\w:]+")
@app.route("/")
def home():
    return "OK"
@app.route("/new", methods = ['POST'])
def new():
    user = str(request.form['user'])
    password = str(request.form['password'])
    return str(assign_wallet(user, password))
@app.route("/transact", methods = ['POST'])
def tr():
    _from = str(request.form['from'])
    if pattern.findall(_from) != []:
        return 'NO'
    to = str(request.form.get('to', False))
    amoun = str(request.form.get('amount', False))
    password = str(request.form.get('password', False))
    if int(amount(_from)) >= int(amoun) and hashlib.sha256(password.encode()).hexdigest() == folderbase.read(_from).split(',')[1]:
        transact(_from, to, int(amoun), password, bypass=False)
        return 'OK'
    else:
        return 'NO'
@app.route("/amount", methods= ["POST"])
def am():
    user = request.form['user']
    return str(amount(user))
@app.route("/nr", methods= ["POST"])
def amy():
    return str(folderbase.read('n'))
@app.route('/auth', methods= ["POST"])
def au():
    ah = request.form['user']
    password = request.form['password']
    if pattern.findall(ah) != []:
        return 'NO'
    if ah != '':
        if auth(ah, password):
            return 'OK'
    return 'NO'


app.run("0.0.0.0", 9314, True)
