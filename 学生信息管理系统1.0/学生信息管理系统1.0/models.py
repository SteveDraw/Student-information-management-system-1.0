from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

db=declarative_base()#这个是sqlalchemy内部封装的一个方法，通过其构造一个基类，这个基类和它的子类，可以将Python类和数据库表关联映射起来

class STU(db):#在所选定的数据库，利用这个类模型建立数据表，并定义其中的类属性对应表中的字段属性
    __tablename__='stu'#将该表命名为stu

    id=Column(Integer,primary_key=True)#数据表的内置的序号，按输入顺序排的，作为关系表的主键
    name=Column(String(64))#
    number=Column(Integer,unique=True)#由于学号是唯一的，并且我们以学号作为搜索的参考，所以用unique设为True，不能重复该值
    math=Column(Integer)
    chinese=Column(Integer)
    english=Column(Integer)





