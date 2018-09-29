
 把页面中url:"http://jqzh.s3.natapp.cc/get_image",改成跑接口的ip和端口，这里我是用natapp生成的
 在output文件夹中python3 -m http.server  8000在output中运行这条命令便可以生成一个简单的http服务器
 在input文件夹中python3 -m http.server  8001在output中运行这条命令便可以生成一个简单的http服务器 
 runApi中的图片存取地址需要改变
 将runApi中的source就是input 中http的ip和端口，url就是output中生成的http ip和端口
 接口 直接运行runApi.py就可以,然后页面上传一张照片就可以在output中看到结果，如果是局域网跑0.0.0.0这条语句
 否则可能需要内网穿透等。
可以使用natapp进行跨域.



 flask 跨域问题,一种是调用flask_cors包就像是runApi2.py,另一种方法就是用@after_request然后加上跨域信息
把下面的模型放到当前目录下
链接:https://pan.baidu.com/s/1mrrN71nJQgZnCPrsmT2O-g  密码:v1xk
