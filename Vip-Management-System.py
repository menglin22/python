import os
import time
print("*********第一次登录请设置管理员*********")
user=input("请设置管理员账号:")
passwd=input("请设置管理员密码:")
users=[""]
passwds=[""]
users.insert(0,user)
passwds.insert(0,passwd)
users.pop(1)
passwds.pop(1)
print("设置成功!")
print("管理员账号为:"+users[0])
print("管理员密码为:"+passwds[0])
input('输入回车键清屏')
os.system("cls")
while 1:
    os.system("cls")
    user=input("请输入用户名(输入exit退出):")
    if (user=="exit"):
        os.system("cls")
        i=5
        while (i>=0):
            print("谢谢使用本系统",end="%d"%(i))
            time.sleep(1)
            os.system("cls")
            i-=1
        exit()
    passwd=input("请输入密码:")
    if user==users[0]:
        if passwd==passwds[0]:
            print("*********登录成功，欢迎管理员*********")
            while 1:
                print("""
    *********操作目录*********
    1.添加会员信息
    2.删除会员信息
    3.查看会员信息
    4.修改会员信息
    5.修改管理员信息
    exit.退出
                """)
                option=input(">>>")
                if(option=="1"):
                    print("*********添加会员信息操作*********")
                    user=input("用户名>>>")
                    passwd=input("密码>>>")
                    if user in users:
                        print("添加失败，用户已存在")
                    else:
                        users.append(user)
                        passwds.append(passwd)
                        print("用户添加成功,现在共有%d个用户"%(len(users)))
                if(option=="2"):
                    print("*********删除会员操作*********")
                    user=input("请输入用户名>>>")
                    if user in users:
                        passwds.pop(users.index(user))
                        users.remove(user)
                        print("用户删除成功,现在共有%d个用户"%(len(users)))
                    else:
                        print("用户不存在")
                if(option=="3"):
                    print("*********查看会员操作*********")
                    print("序号\t用户名\t密码")
                    for user in users:    
                        print("%d\t%s\t%s"%(users.index(user)+1,user,passwds[users.index(user)]))
                if(option=="4"):
                    print("*********修改会员操作*********")
                    user=input("请输入用户名>>>")
                    vipnum=users.index(user)
                    if(vipnum==0):
                        print("此操作无法修改管理员的信息")
                    elif user in users:
                        user=input("请输入新用户名>>>")
                        users.pop(vipnum)
                        users.insert(vipnum,user)
                        passwd=input("请输入新密码>>>")
                        passwds.pop(vipnum)
                        passwds.insert(vipnum,passwd)
                        print("用户信息更新")
                    else:
                        print("用户不存在")
                if(option=="5"):
                    print("*********查看会员操作*********")
                    user=input("请输入新用户名>>>")
                    users.pop(0)
                    users.insert(0,user)
                    passwd=input("请输入新密码>>>")
                    passwds.pop(0)
                    passwds.insert(0,passwd)
                    print("管理员信息更新")
                if(option=="exit"):
                    user=""
                    passwd=""
                    break
    if user in users:
        if (passwd==passwds[users.index(user)]):
            print("*********登录成功,欢迎"+user)
            while 1:
                print("""
1.查看个人信息
exit.退出
""")
                option=input(">>>")
                if(option=="1"):
                    print("*********查看个人信息操作*********")
                    print("序号\t账号\t密码")
                    print("%d\t%s\t%s"%(users.index(user)+1,user,passwd))
                if(option=="exit"):
                    user=""
                    passwd=""
                    break
    
