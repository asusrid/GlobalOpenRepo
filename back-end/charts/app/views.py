# #from app import app
# from flask import Flask, send_file, make_response, render_template
# from mycharts import makePlot
# app = Flask(__name__)
#
#
# @app.route('/', methods=['GET'])
# def home():
# 	bytes_obj = makePlot()
# 	return send_file(bytes_obj, attachment_filename='plot.png', mimetype='image/png')
#
# @app.route('/template')
# def template():
#     return render_template('home.html')
#
# if __name__ == '__main__':
#     app.run(debug=False)