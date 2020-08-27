import flask
import waitress
import os
import urllib
from flask import Flask, render_template, send_from_directory, request, redirect
from requests import get
from waitress import serve
from data.constants import constants, pack_changelog

app = Flask(__name__, 
	static_folder='static', 
	template_folder="templates"
) 

a = constants()

# 		========================

# special case routes for root files

@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/favicon.ico')
def static_from_root():
	return send_from_directory(app.static_folder, request.path[1:])


# basic routes

@app.route('/')
def index(): 
	return render_template('index.html', a = a)

@app.route('/sitemap')
def sitemap(): 
	return render_template('sitemap.html', a = a)

@app.route('/minecraft')
def minecraft(): 
	return render_template('minecraft.html', a = a)

@app.route('/trashbot')
def trashbot(): 
	return render_template('trashbot.html', a = a)

@app.route('/pack')
def pack(): 
	return render_template('pack.html', a = a)

@app.route('/pack/changelog')
def packchangelog(): 
	c = pack_changelog()
	return c.changelog_page

@app.route('/gmod')
def gmod(): 
	return render_template('gmod.html', a = a)

@app.route('/donors')
def donors(): 
	return render_template('donors.html', a = a)

@app.route('/styles')
def style(): 
	return render_template('style.html', a = a)

@app.route('/funny')
def funny(): 
	funnyarg = request.args.get('f')
	return render_template('extra/funny.html', funnyarg = funnyarg, a = a)

@app.route('/gmodload')
def gmodload(): 
	return render_template('extra/gmodload.html', a = a)

@app.route('/tf2motd')
def tf2motd(): 
	return render_template('extra/tf2motd.html', a = a)


# routes to redirects and redirect templates

@app.route('/gmodsrv')
def redirect_gmod(): 
	return render_template('redirects/gmodsrv.html', a = a)

@app.route('/rhc')
def redirect_rhc(): 
	return render_template('redirects/rhc.html', a = a)

@app.route('/trashbot/commands')
def redirect_trashbot_cmds():
  return get(a.trashbot_cmds).content


# routes to error templates

@app.errorhandler(403)
def forbidden(error):
	return render_template('errors/403.html', error = error, a = a), 403

@app.errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html', error = error, a = a), 404

@app.errorhandler(500)
def internal_server(error):
	return render_template('errors/500.html', error = error, a = a), 500


# 		========================

if __name__ == '__main__':
	serve(app, host='0.0.0.0', port=8080)		# waitress (production)
#	app.run(host="0.0.0.0", port="8080")		# flask (development)