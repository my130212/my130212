from flask_sqlalchemy import SQLAlchemy
from flask import Flask

class Config(object):
	"""项目的配置"""
	Debug = True

	#为数据库添加配置
	SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/3306/mydb'

	SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
#加载配置
app.config.from_object(Config)
#初始话数据库
db = SQLAlchemy(app)

@app.route("/")
def index():
	return "<h1 style='color:red'>Hello World</h1>"

if __name__ == "__main__":
	app.run()
