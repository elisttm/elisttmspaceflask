from __main__ import app, flask, a
import urllib
import urllib.request

# 		========================

cat_url = "http://cat.elisttm.space:7777/"

# 		========================

@app.route('/cats')
def randomcats(): 
	return flask.render_template('cats.html', cat_url = cat_url, status = urllib.request.urlopen(cat_url).getcode(), a = a)
