from __main__ import app, flask, a
import urllib, urllib.request

# 		========================

cat_url = "http://e.elisttm.space:7777/"

# 		========================

@app.route('/cats')
def randomcats():
	return flask.render_template('cats.html', cat_url = cat_url, a = a)
