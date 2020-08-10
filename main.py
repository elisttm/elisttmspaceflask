import flask
import waitress
import tinydb
from flask import Flask, render_template, send_from_directory, redirect
from waitress import serve
from tinydb import TinyDB, Query
from tinydb.operations import increment
from data.constants import const

app = Flask(__name__)

db = TinyDB('data/database.json')
query = Query()

# 		========================

@app.route('/')
@app.route('/home')
@app.route('/index')
def index(): 
	return render_template('index.html', a = const())

@app.route('/minecraft')
def minecraft(): 
	return render_template('minecraft.html', a = const())

@app.route('/trashbot')
def trashbot(): 
	return render_template('trashbot.html', a = const())

@app.route('/pack')
def pack(): 
	return render_template('pack.html', a = const())

@app.route('/donors')
def donors(): 
	return render_template('donors.html', a = const())

@app.route('/funny')
def funny(): 
	return render_template('funny.html', a = const())

@app.route('/template')
def template(): 
	return render_template('template.html', a = const())

# 		========================

@app.route('/gmod')
def gmod(): 
	return render_template('redirects/gmod.html', a = const())

@app.route('/raymond')
def raymond(): 
	return render_template('redirects/raymond.html', a = const())

# 		========================

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', error = error, a = const()), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', error = error, a = const()), 404

@app.errorhandler(500)
def internal_server(error):
    return render_template('errors/500.html', error = error, a = const()), 500

# 		========================

if __name__ == '__main__':
	serve(app, host='0.0.0.0', port=8080)
#	app.run(host="0.0.0.0", port="8080")