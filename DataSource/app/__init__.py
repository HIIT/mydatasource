"""
    @project Data Source
    @author Xiaoxiao Xiong
    @date 10/08/2015
    @version 0.1
    <pre><b>email: </b>shawnhsiung07@gmail.com</pre>
    <pre><b>company: </b>DHR</pre>
    @brief
"""

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from dhr_logging.logger import DHRLogger

from app.config import APP_NAME
from app.config import SECRET_KEY
from app.config import SQLALCHEMY_DATABASE_URI
from app.config import SQLALCHEMY_COMMIT_ON_TEARDOWN

app = Flask(__name__)

api = Api(app, prefix='/api/v0.1')

app_log = DHRLogger.getLogger('dhr.source')

app.config['APP_NAME'] = APP_NAME
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = SQLALCHEMY_COMMIT_ON_TEARDOWN
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

from views import api_0_1

app.register_blueprint(api_0_1)

# CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods','GET,POST,PUT,DELETE')
    return response

# Exposes all resources matching /api/v0.1 to CORS
# CORS(app,resources={r'/*':{'origins':'*'}},allow_headers='*')

@app.errorhandler(404)
def error_404(error):
    return jsonify({'status_code': '404', 'message': 'Not found'}), 404

db.create_all()