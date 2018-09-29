
import flask
import json
from flask import Flask,jsonify,request

from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/get_image',methods=['post','get','OPTIONS'])#指定接口访问的路径，支持什么请求方式get，post
# @app.route('/get_image')
def get_image():

     if request.method=='OPTIONS':
          res=flask.make_response()
     if request.method=="POST":
          print("success!!!!!!")
          # data=request.files['image']
          # print(data.filename)
          data1 = {
               'name': 'ACME',
               'shares': 100,
               'price': 542.23
          }
     return json.dumps(data1)

app.run(host='0.0.0.0',port=8802,debug=True)











































