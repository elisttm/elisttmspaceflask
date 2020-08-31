from __main__ import app, flask, a

# 		========================

donor_list = (
	"($10) Tao Scree", 
	"($2) SoFluffer"
)

# 		========================

@app.route('/donors')
@app.route('/donors/')
def donors(): 
	return flask.render_template('donors.html', a = a, donor_list = donor_list)
