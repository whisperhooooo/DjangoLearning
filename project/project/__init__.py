import pymysql
pymysql.install_as_MySQLdb()#使用MySQL 在setting.py文件中进行数据库配置

from .celery import app as celery_app