import flask
import waitress
import tinydb
import os
from flask import Flask, render_template, send_from_directory, send_file, redirect, request
from waitress import serve
from tinydb import TinyDB, Query
from tinydb.operations import increment
from data.constants import constants, pack_changelog

app = Flask(__name__, static_folder='static', template_folder="templates") 

db = TinyDB('data/database.json')
query = Query()

# 		========================


# special case routes for root files

@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/favicon.ico')
def static_from_root():
	return send_from_directory(app.static_folder, request.path[1:])


# basic routes

@app.route('/')
@app.route('/home')
def index(): 
	return render_template('index.html', a = constants())

@app.route('/sitemap')
def sitemap(): 
	return render_template('sitemap.html', a = constants())

@app.route('/minecraft')
def minecraft(): 
	return render_template('minecraft.html', a = constants())

@app.route('/trashbot')
def trashbot(): 
	return render_template('trashbot.html', a = constants())

@app.route('/pack')
def pack(): 
	return render_template('pack.html', a = constants())

@app.route('/pack/changelog')
def packchangelog(): 
	c = pack_changelog()
	return c.changelog_page

@app.route('/donors')
def donors(): 
	return render_template('donors.html', a = constants())

@app.route('/style')
def style(): 
	return render_template('style.html', a = constants())

@app.route('/funny')
def funny(): 
	funnyarg = request.args.get('f')
	return render_template('extra/funny.html', funnyarg = funnyarg, a = constants())

@app.route('/gmodload')
def gmodload(): 
	return render_template('extra/gmodload.html', a = constants())


# routes to redirect templates

@app.route('/gmod')
def redirect_gmod(): 
	return render_template('redirects/gmod.html', a = constants())

@app.route('/raymond')
def redirect_raymond(): 
	return render_template('redirects/raymond.html', a = constants())


# routes to error templates

@app.errorhandler(403)
def forbidden(error):
	return render_template('errors/403.html', error = error, a = constants()), 403

@app.errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html', error = error, a = constants()), 404

@app.errorhandler(500)
def internal_server(error):
	return render_template('errors/500.html', error = error, a = constants()), 500


# 		========================

if __name__ == '__main__':
	serve(app, host='0.0.0.0', port=8080)		# waitress (production)
#	app.run(host="0.0.0.0", port="8080")		# flask (development)