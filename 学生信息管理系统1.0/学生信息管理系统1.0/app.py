from models import STU#引入STU类，便于使用事物session操作
from __init__ import session,engine#__init__为同目录下的数据库配置和连接模块

def stu_information():  # 输入和保存学生相关信息的函数，此为该系统的重要数据部分
    name = input("请输入该学生的姓名：")
    number = input("请输入该学生的学号：")
    math = input("请输入该学生的数学成绩：")
    chinese = input("请输入该学生的语文成绩：")
    english = input("请输入该学生的英语成绩：")
    user = STU(name=name, number=number, math=math, chinese=chinese, english=english)#左边的name是数据库(模型类)对应的列名name，右边name是我们input收集的变量
    session.add(user)
    session.commit()
    print('>>添加成功！\n')

def stu_change():  # 修改单个学生信息功能的函数
    numbers = input("请输入该学生的学号：")
    users = session.query(STU).filter_by(number=numbers).first()#先查找出对应学号的对象，在重新添加信息覆盖之前的信息，达到修改的目的
    users.name = input("请输入该学生的姓名：")
    users.math = input("请输入该学生的数学成绩：")
    users.chinese = input("请输入该学生的语文成绩：")
    users.english = input("请输入该学生的英语成绩：")
    session.add(users)
    session.commit()
    return

def stu_delete():  # 删除相关信息功能的函数
    numbers = eval(input("请输入要删除学生信息的序号："))
    result=session.query(STU).filter_by(number=numbers).first()
    if result != None:#若返回对象不为为空，继续删除操作
        session.delete(result)
        session.commit()
        print('>>删除成功')
    else:
        print('>>查无此人或你的输入有误！')

def stu_check():  # 查找相关信息的函数
    numbers = input("请输入要查询学生信息的序号：")
    result=session.query(STU).filter_by(number=numbers).first()
    if result != None:
        print('-' * 56)
        print('|{0:^22}|{1:^6}|{2:^6}|{3:^5}|{4:^5}|'.format('姓名', '学号', '数学', '语文', '英语'))
        print('-' * 56)
        print('|{0:^20}\t|{1:^6}\t|{2:^6}\t|{3:^6}\t|{4:^6}|'.format(result.name, result.number, result.math,result.chinese, result.english))
        print('-' * 56)
    else:
        print('>>查无此人或你的输入有误！')

def stu_all(*b):  # 显示该系统中的所有学生信息数据
    all_result=session.query(STU).all()
    print('<全部学生成绩表>' .center(52,'—'))
    print('|{0:^22}|{1:^6}|{2:^6}|{3:^5}|{4:^5}|'.format('姓名','学号','数学','语文','英语'))#为了输出效果上构成一个表，输出格式进行了对应的调整
    print('-' * 56)#该表的横线分隔部分是由‘-’构成，如果想用其他符号也可（+=）
    for i in all_result:
        print('|{0:^20}\t|{1:^6}\t|{2:^6}\t|{3:^6}\t|{4:^6}|'.format(i.name, i.number, i.math, i.chinese,i.english))
        print('-' * 56)
    print(">>已显示系统内所有人的信息！\n")

def stu_rank():  # 排序不同类型成绩的函数
    lists=[]#用于存储转换后的单个信息列表的列表
    rank_count=0#用于排名表遍历输出次序设定的初始值
    rank_result=engine.execute('select *,(math+chinese+english) 总成绩 from stu order by 总成绩 desc')#返回多个元组构成的结果，包含各个信息和总分
    for i in rank_result:
        p=list(i)#将单个元组转换成列表（数组），便于后面索引得到想要的数据
        lists.append(p)
    print('<总分排名表>'.center(70,'='))#该表的横线分隔部分是由‘=’构成，如果想用其他符号也可（+-），不过实验过对于这个表这种效果比较好
    print('|{0:^22}|{1:^6}|{2:^6}|{3:^5}|{4:^5}|{5:^8}|{6:^5}|'.format('姓名','学号','数学','语文','英语','总分','排名'))
    print('=' * 73)
    for k in lists:
        rank_count+=1#每次遍历按总分降序出来的列表，遍历时记录操作，赋予对应的排名值
        print('|{0:^20}\t|{1:^6}\t|{2:^6}\t|{3:^6}\t|{4:^6}|{5:^9}|{6:^6}|'.format(k[1],k[2],k[3],k[4],k[5],k[6],rank_count))
        print('=' * 73)
    print(">>已显示系统内所有人的总分排名信息！\n")

while True:  # while循环使功能主界面能一直供用户使用，直到用户不需要为止
    print('学生成绩管理系统，请选择系统功能'.center(71,'-'))#功能选项也是在一个方框内
    print('{0:<3}{1:<72}\t{2:>}'.format('|','1.输入学生信息;','|'))
    print('{0:<3}{1:<69}\t{2:>}'.format('|','2.修改学生的相关信息;','|'))
    print('{0:<3}{1:<69}\t{2:>}'.format('|','3.删除学生的相关信息;','|'))
    print('{0:<3}{1:<69}\t{2:>}'.format('|','4.查询学生信息;','|'))
    print('{0:<3}{1:<69}\t{2:>}'.format('|','5.显示所有学生的信息;','|'))
    print('{0:<3}{1:<72}\t{2:>}'.format('|','6.学生成绩排序;','|'))
    print('{0:<3}{1:<72}\t{2:>}'.format('|','0.退出程序;','|'))
    print('-'*80,'\n')
    select = input("请输入你的功能选择>>")
    if select == '1':
        stu_information()  # 函数调用或传参使用
    elif select == '2':
        stu_change()    #同上
    elif select == '3':
        stu_delete()
    elif select == '4':
        stu_check()
    elif select == '5':
        stu_all()
    elif select == '6':
        stu_rank()
    elif select == '0':
        print('\n','本系统版本:version1.0'.center(65,'-'))
        print("感谢你的使用！！！祝你考试旗开得胜！！！")
        print("开发者:SteveDraw,么么哒^_^")
        print('-'*70)
        break
    else:
        print(">>你的输入错误！请按照提示重新输入！\n")  # 错误输入格式提醒
        continue
