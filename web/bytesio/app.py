from flask import Flask, render_template, send_file, make_response
from io import StringIO, BytesIO
import matplotlib.pyplot as plt
from base64 import b64encode
# from StringIO import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', base_url=BASE_URL)


def make_fig():
    plt.plot([1,2,3,4], [1,2,3,4])
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    # buffer = b''.join(buf)
    # b2 = b64encode(buffer)
    # img = b2.decode('utf-8')
    # return render_template('index.html', img=img)
    return buf

@app.route('/show_plot', methods=['GET'])
def show_plot():
    bytes_obj = make_fig()
    return send_file(bytes_obj, attachment_filename='plot.png', mimetype='image/png')




# @app.route('/fig/<cropzonekey>')
# def fig(cropzonekey):
#     fig = draw_polygons(cropzonekey)
#     img = StringIO()
#     fig.savefig(img)
#     img.seek(0)
#     return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=False)
