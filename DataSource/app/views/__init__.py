"""
    @package views
    @author Xiaoxiao Xiong
    @date 14/08/2015
    @version 0.1
    <pre><b>email: </b>shawnhsiung07@gmail.com</pre>
    <pre><b>company: </b>DHR</pre>
    @brief the purpose of views is to provide API for Data Operator,
    Data Sink and users of Data Source
"""


from flask import Blueprint

api_0_1 = Blueprint('api', __name__)

from app.views import category, contract, data, label, receipt, resource, resource_set, service, units, user