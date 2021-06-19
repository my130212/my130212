import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_redis import FlaskRedis
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from config import config

#初始话数据库
db = SQLAlchemy()
redis_store = None

def set_log(config_name):
	#设置日志的等级
	logging.basicConfig(level=config[config_name].LOG_LEVEL)
	#创建记录器对象
	logger = logging.getLogger()
	#创建处理器对象
	Handler = RotatingFileHandler("logs/log",maxBytes = 1024 * 1024 * 100,backupCount = 10)
	#创建格式化器对象
	Format = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
	#将格式化器加载给处理器对象
	Handler.setFormatter(Format)
	#将处理器加载给记录器对象
	logger.addHandler(Handler)

def creat_app(config_name):
	#设置日志
	set_log(config_name)
	#创建app对象
	app = Flask(__name__)
	#加载配置
	app.config.from_object(config[config_name])
	#数据库添加配置
	db.init_app(app)
	#初始话redis数据库存储
	global redis_store
	redis_store = FlaskRedis(app)
	#开启当前项目 csrf 保护，只做服务器验证功能
	CSRFProtect(app)
	#设置Session的指定保存位置
	Session(app)

	#导入蓝图并且注册蓝图（防止出现循环导入的错误）
	from info.models.index import index_blu
	app.register_blueprint(index_blu)

	return app
