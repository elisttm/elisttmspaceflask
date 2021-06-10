import flask
import waitress
import os
import json
import urllib, urllib.request
#import requests
from flask import Flask, render_template, send_from_directory, request, redirect, make_response, Markup
#rom requests import get
from waitress import serve
from data.constants import constants

# 		========================

app = Flask(__name__, 
	static_folder='static', 
	template_folder="templates"
) 

a = constants()

def convert_plaintext(content:str):
	content = make_response(content, 200)
	content.mimetype = "text/plain"
	return content

# 		========================

# special case routes for root files

@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/favicon.ico')
def static_from_root():
	return send_from_directory(app.static_folder, request.path[1:])

# 		========================

if __name__ == '__main__':
	import routes
	serve(app, host='0.0.0.0', port=8080)		# waitress (production)
#	app.run(host="0.0.0.0", port="8080")		# flask (development)