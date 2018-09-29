import os,io
from flask import Flask,Response,request,send_file,send_from_directory
import checkpoint_1
from utils import  main
import json
import random

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
     if request.method=="POST":
          # 获取前端传来的数据
          print("success!!!!!!")
          random_num=random.randint(1,9999999)
          data1 = {}
          data=request.files['image']
          type = request.values.get('type')
          # print('1')
          input_path="/home/hadoop/Desktop/jiekou/output/"
          out_path = "/home/hadoop/Desktop/jiekou/output/"

          print(os.path.join(input_path,data.filename))
          # 获取图片后缀
          suddix = str(data.filename).split('.')[-1]
          print('dadads', suddix)

          save_path=os.path.join(input_path,'source'+str(random_num)+'.'+suddix)
          data.save(save_path)
          print('存储完成')
          i = checkpoint_1
          a = i.checkpoint()
          print("修改checkpoint参数******--------------")
          print(os.getcwd())
          a.checkpoint_dir = os.path.join(a.checkpoint_dir1, str(type))
          a.in_path = save_path


          a.out_path = os.path.join(out_path,'url'+str(random_num)+'.'+suddix)

          print("*******************",os.path.join(out_path,'url'+str(random_num)+'.'+suddix))
          print('a.checkpoint_dir:',a.checkpoint_dir)
          print(a.in_path)
          print(a.out_path)
          main(a)
          print("修改完成******--------------")

          map={}
          url=str(os.path.join('http://jqzh326.s3.natapp.cc','url'+str(random_num)+'.'+suddix))
          source=str(os.path.join('http://jqzh326.s3.natapp.cc','source'+str(random_num)+'.'+suddix))
          map["url"]=url
          map["source"]=source
          json_str=json.dumps(map)
          print("source",source)
          print("url",url)
          return json_str
          # 返回图片文件
          # img_stream = return_img_stream(os.path.join(out_path, data.filename))
          # response=app.make_response(img_stream)
          # return response
     return '<h1>Hello Word!!<h1>'
     # return send_from_directory(out_path,data1.filename,as_attachment=True)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

# app.run()

# app.run(host='0.0.0.0',port=8802,debug=True,threaded=False)
app.run(host='127.0.0.1',port=8802,debug=True,threaded=False)











































