from . import index_blu
from ... import redis_store


@index_blu.route("/")
def index():
	redis_store['my'] = 28
	return "<h1 style='color:red'>Hello World</h1>"
