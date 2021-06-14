from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flaskext import csrf
from flask_wtf.csrf import CSRFProtect
from flask import Flask

class Config(object):
	"""项目的配置"""
	Debug = True

	#为数据库添加配置
	SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/3306/mydb'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	#添加redis数据的配置
	REDIS_HOST = '127.0.0.1'
	REDIS_PORT = 6379

app = Flask(__name__)
#加载配置
app.config.from_object(Config)
#初始话数据库
db = SQLAlchemy(app)
#初始话redis数据库存储
redis_store = FlaskRedis(app)
#开启当前项目 csrf 保护，只做服务器验证功能
CSRFProtect(app)

@app.route("/")
def index():
	return "<h1 style='color:red'>Hello World</h1>"

if __name__ == "__main__":
	app.run()
