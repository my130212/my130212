from flask import blueprints
#������ͼ����
index_blu = blueprints.Blueprint('index', __name__)

from . import views
