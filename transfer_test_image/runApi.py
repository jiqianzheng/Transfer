import os
import flask
import json
from flask import Flask,jsonify,request,send_file,send_from_directory
import checkpoint_1
from utils import  main

app = Flask(__name__)


def return_img_stream(img_local_path):
    """
    工具函数:
    获取本地图片流
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """
    import base64
    img_stream = ''
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode('ascii')
    return img_stream


@app.route('/get_image',methods=['post','get','OPTIONS'])#指定接口访问的路径，支持什么请求方式get，post
# @app.route('/get_image')
def get_image():
     if  request.method=='GET':
          return '<h1>Hello Word!!<h1>'

     if request.method=='OPTIONS':
          res=flask.make_response()
     if request.method=="POST":
          # 获取前端传来的数据
          print("success!!!!!!")
          data1 = {}
          data=request.files['image']
          type = request.values.get('type')
          #图片路径
          input_path="/home/hadoop/Desktop/jiekou/input"
          out_path = "/home/hadoop/Desktop/jiekou/output"

          print(os.path.join(input_path,data.filename))
          save_path=os.path.join(input_path,data.filename)
          data.save(save_path)

          i = checkpoint_1
          a = i.checkpoint()
          print("修改checkpoint参数******--------------")
          print(os.getcwd())
          a.checkpoint_dir = os.path.join(a.checkpoint_dir1, str(type))
          a.in_path = save_path
          a.out_path = os.path.join(a.out_path1)
          print("*******************",os.path.join(out_path,data.filename))

          print('a.checkpoint_dir:',a.checkpoint_dir)
          print(a.in_path)
          print(a.out_path)
          main(a)
          print("修改完成******--------------")
          img_stream = return_img_stream(os.path.join(out_path, data.filename))
          response=app.make_response(img_stream)
     return response
     # return send_from_directory(out_path,data.filename,as_attachment=True)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

# app.run()

# app.run(host='0.0.0.0',port=8802,debug=True,threaded=False)
app.run(host='127.0.0.1',port=8802,debug=True,threaded=False)











































