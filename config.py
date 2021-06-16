from redis import StrictRedis


class Config(object):
	"""项目的配置"""
	Debug = True

	SECRET_KEY = 'zRDv7adXxniygRZvZnAZLLVV2fmY8rhNmdkFZ7xBoVk4ivMV4yU5inhKtxCuYdQ+sJYDm324FLerIkHZknS2gg=='

	#为数据库添加配置
	SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/3306/mydb'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	#添加redis数据的配置
	REDIS_HOST = '127.0.0.1'
	REDIS_PORT = 6379

	#session的保存位置
	SESSION_TYPE = 'redis'

	SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db=1)
	#开启session签名
	SESSION_USE_SIGNER = True
	#设置session需过期
	SESSION_PERMANENT = False
	#设置session过期时间
	PERMANENT_SESSION_LIFETIME = 86400 * 2

class DevolopmentConfig(Config):
	"""开发环境项目的配置"""
	Debug = True

class ProductionConfig(Config):
	"""生产环境项目的配置"""
	Debug = False

class TestingConfig(Config):
	"""单元测试环境项目的配置"""
	Debug = True
	TESTING = True

config = {
	'devolopment': DevolopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}
