from flask import Flask
from flask_redis import FlaskRedis
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from config import config

#初始话数据库
db = SQLAlchemy()

def creat_app(config_name):
	app = Flask(__name__)
	#加载配置
	app.config.from_object(config[config_name])
	#数据库添加配置
	db.init_app(app)
	#初始话redis数据库存储
	redis_store = FlaskRedis(app)
	#开启当前项目 csrf 保护，只做服务器验证功能
	CSRFProtect(app)
	#设置Session的指定保存位置
	Session(app)

	return app
