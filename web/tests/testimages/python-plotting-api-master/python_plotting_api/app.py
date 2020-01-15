from flask import Flask, send_file, make_response, render_template
import os
from plotting import get_correlation_matrix_as_bytes, get_breast_cancer_df, get_pair_plot_as_bytes

app = Flask(__name__)

# get data to keep it in memory, usually you will serve this from a database or bucket, or whereever your db is sitting
breast_cancer_df, features_names = get_breast_cancer_df()

env = os.getenv("run_env", "dev")

if env == "dev":
    BASE_URL = "http://localhost:5000/"
elif env == "prod":
    BASE_URL = "https://python-sci-plotting.herokuapp.com/"


@app.route('/')
def index():
    return render_template('index.html', base_url=BASE_URL)


@app.route('/plots/breast_cancer_data/pairplot/features/<features>', methods=['GET'])
def pairplot(features):
    try:
        # parse columns
        parsed_features = [feature.strip() for feature in features.split(',')]
        bytes_obj = get_pair_plot_as_bytes(breast_cancer_df, parsed_features)

        return send_file(bytes_obj,
                         attachment_filename='plot.png',
                         mimetype='image/png')
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request, probably feature names are wrong', 400)


@app.route('/plots/breast_cancer_data/correlation_matrix', methods=['GET'])
def correlation_matrix():
    bytes_obj = get_correlation_matrix_as_bytes(breast_cancer_df, features_names)

    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')


if __name__ == '__main__':
    if env == "dev":
        app.jinja_env.auto_reload = True
        app.config['TEMPLATES_AUTO_RELOAD'] = True
        app.run(debug=True)
    else:
        app.run(debug=False)
