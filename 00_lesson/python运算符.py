#coding:utf-8
'''
运算符（5种）：1.算数运算符   2.关系运算符   3.赋值运算符  4.成员运算符  5.逻辑运算符
'''
'''
1.算数运算符（7个）
 +      -      *      /       %       **            //
 加    减     乘      除      取余    幂运算       取整
'''
print '1+1=',1+1
print '2-2=',2-2
print '2*2=',2*2
print '1/2=',1.0/2 #若被除数与除数都为int类型时，结果也会为int类型，如果需要打印小数，那么被除数与除数其中一个必须为float类型
print '10%3=',10%3
print '2**2=',2**2
print '10//3',10//3
print "==================分割线===================="

'''
关系运算符（7个）  运算结果返回布尔值（True或False）
  <           >            <=           >=            !=           <>           ==
 小于       大于         小于等于      大于等于       不等于       不等于        相等
'''
print '1<2',1<2
print 1>2
print 1<=2
print 1>=2
print 1!=2
print 1<>2
print 1==2
print "==================分割线===================="

'''
赋值运算符(8个)
 =        +=            -=          *=            /=         %=           //=         **=
等号      加等          减等        乘等          除等        取余等       取整等       幂运算等
'''
a = 1
a+=1  #同 a=a+1
print a
b = 2
b-=1  #同 b=b-1
print b
print "==================分割线===================="

'''
成员运算符（2个）  返回结果为布尔值
in 在该有序数组内
not in 不在该有序数组内
'''
c = [1,2,[3,4]]
print 1 in c #True
print 3 in c #
print 4 in c
print [3,4] in c
print 2 not in c
print "==================分割线===================="

'''
逻辑运算符（3个）
and  与   例：a and b若整体要为True,则a与b都应为True，否则结果为False
or   或   例：a or b若整体要为True,则a与b至少一个为True，否则结果为False
not  非   例： not a若要为True，那么a本身为False
'''
a = 1<2 #True
b = 1>2 #Flase
print a and b
print a or b
print not a
