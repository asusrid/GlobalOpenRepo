from app.blueprints.core.bp import bp
from app.blueprints.core.mycharts import makePlot, animatedLineplot
from flask import Flask, send_file, make_response, render_template


@bp.route('/example')
def exampleRoute():
    bytes_obj = makePlot()
    return send_file(bytes_obj, attachment_filename='plot.png', mimetype='image/png')


@bp.route('/animatedlineplot')
def animatedLineplotRoute():
	return animatedLineplot()
    #bytes_obj = animatedLineplot()
    #return send_file(bytes_obj, attachment_filename='plot.png', mimetype='image/png')