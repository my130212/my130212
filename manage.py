import logging

from flask import session,current_app
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from info import creat_app,db

#创建app，配置不同环境的配置
app = creat_app('devolopment')
#使用项目管理器管理app
manage = Manager(app)
#设置迁移Migrate对象,将app与db相关联
migrate = Migrate(app,db)
#将迁移命令添加到manager对象中
manage.add_command('db',MigrateCommand)

if __name__ == "__main__":
	manage.run()
