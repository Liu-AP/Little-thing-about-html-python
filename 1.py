from flask import Flask
from flask import request
from flask_cors import CORS #导入解决跨域问题的模块
app = Flask(__name__)

CORS(app, supports_credentials=True) #动态解决前端跨域问题
app.debug = True #开启flask调试模式
@app.route('/',methods=['post']) #指定请求路径、方法
def add_stu():
    a = request.values.get("fir")
    b = request.values.get("sec")  

    return str(int(a) + int(b))
if __name__ == '__main__':
    app.run(host='localhost',port=1234)#指定端口号和地址

