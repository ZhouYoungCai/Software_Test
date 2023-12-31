#coding:utf-8
'''
程序结构：3种
1.顺序结构：即语句从上到下按顺序执行
2.分支结构：一条大路，会有很多分支路口。在Python中常用if elif else 判断语句
3.循环结构：如歌曲/歌单循环播放。在Python中常用while循环和for循环
'''
'''
2.分支结构：if条件语句：若满足对应条件，则执行对应语句
'''
#①未分支前
#格式：
#if 条件语句:  （注意条件语句后有冒号）
        #   对应语句   （注意对应语句需要缩进）

# if 1<2: #当1>2为假的时候，下面对应的语句则不会执行
#     print "当if条件为真的时候，我才会打印" #使用缩进表示代码块，属于if代码块下的内容
# print "这个print是一个新的代码块，什么时候都会打印，不受上面的条件影响"

#②if else分支
'''格式:
if 条件语句:
    对应语句1
else:
    对应语句2
'''
# if 1>2:
#     print "如果if条件为真的话，我就会打印"
# else:
#     print "如果if条件为假的话，我就会被打印"

#③if elif else 分支结构（其中elif可以分支很多条路）
'''
格式：
if 条件语句1:
    对应语句1
elif 条件语句2:
    对应语句2
elif 条件语句3:
    对应语句3
    .......
else:
    对应语句n
'''
sex = raw_input("请输入你的性别：")
if sex=="male":
    print "你的性别是男"
elif sex=="female":
    print "你的性别是女"
else:
    print "性别输入错误"