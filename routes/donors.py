from __main__ import app, flask, a

# 		========================

# impliment patreon api to automatically get patrons + amounts

donor_list = (
	"($20) Tao Scree", 
	"($3) SoFluffer"
)

# 		========================

@app.route('/donors')
@app.route('/donors/')
def donors(): 
	return flask.render_template('donors.html', donor_list = donor_list, a = a)
