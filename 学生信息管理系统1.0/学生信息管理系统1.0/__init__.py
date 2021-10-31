from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db#models为同目录下的数据库模型模块文件
engine=create_engine('mysql+pymysql://root:<你的mysql的登录密码>@localhost/sqltest')#数据库连接引擎，根据自己所选的数据库配置即可
DbSession = sessionmaker(bind=engine)
session = DbSession()#session用于创建程序和数据库之间的会话，所有对象的载入和保存都需要通过session对象
db.metadata.create_all(engine)#创建数据表，原本存在即忽略