#coding:utf-8
'''
切片，截取，切片与截取基于index下标索引进行截取字符串的一部分或者全部，python的index从0开始计算位数
格式： 变量名[index]
'''
#1.正序切片:
a = "Hello"
print a[1] #切取单个内容
print a[0:3] #切取下标索引为0~3之间不包括3的内容
print a[:3] #从左边0开始切片直到切取到有边界值以内的值，不包括边界值
print a[0:] #从下标索引为0数据开始，切片直到最后一位为止

#2.倒序切片
#就是把下标索引倒过来即最后一位为-1，倒数第二位为-2，依次类推，下标索引可以倒序，但不能反切
#（必须按照原有变量中的顺序进行切片）
print a[0:-3] #下标所有右到左算，倒数第三位为边界值，切取后剩He
print a[0:-2]

#3. 切完整的Hello方法：
print a[0:]
print a[:]
print a[0:5]

#字符串支持的方法:
#1.加法运算
a = "Hello"
b = "python"
c = a+b #将a,b两个字符串进行合并，编程一个新的字符串
# print c,type(c)
print a+' '+b,type(a+b)

#2.乘法运算
print c*2


