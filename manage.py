from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flaskext import csrf
from flask_wtf.csrf import CSRFProtect
from flask import Flask,session
from flask_session import Session
from redis import StrictRedis
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from config import Config

app = Flask(__name__)
#加载配置
app.config.from_object(Config)
#初始话数据库
db = SQLAlchemy(app)
#初始话redis数据库存储
redis_store = FlaskRedis(app)
#开启当前项目 csrf 保护，只做服务器验证功能
CSRFProtect(app)
#设置Session的指定保存位置
Session(app)
#使用项目管理器管理app
manage = Manager(app)
#设置迁移Migrate对象,将app与db相关联
migrate = Migrate(app,db)
#将迁移命令添加到manager对象中
manage.add_command('db',MigrateCommand)



@app.route("/")
def index():
	session['nan'] = '26'
	return "<h1 style='color:red'>Hello World</h1>"

if __name__ == "__main__":
	manage.run()
