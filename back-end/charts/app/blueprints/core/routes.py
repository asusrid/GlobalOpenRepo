from app.blueprints.core.bp import bp
from app.blueprints.core.mycharts import makePlot
from flask import Flask, send_file, make_response, render_template


@bp.route('/')
def home():
    bytes_obj = makePlot()
    return send_file(bytes_obj, attachment_filename='plot.png', mimetype='image/png')