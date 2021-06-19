from flask import blueprints
#创建蓝图对象
index_blu = blueprints.Blueprint('index', __name__)

from . import views
