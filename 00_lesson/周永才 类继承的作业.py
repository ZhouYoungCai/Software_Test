1. ����һ��ģ��person������һ��people����	
������������name�����height������weight ��
�෽��������work����Ϣrest��
���� women�̳�people�࣬
��д����:�����������µķ������
�ټ���һ������man��ͬʱ�̳�people����women�࣬
����������ˮ��
����һ���µ�ģ��dyp����person�е������࣬
����������ֱ���ж��󴴽������ø���������з�����
#coding:utf-8
class person:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
        print "�������"
    def work(self):
        print "��%s�Ĺ�����������Թ���ʦ" %self.name
    def rest(self):
        print "����Ϣ���ܳ��ߣ��ҵ������%d����" %self.height

class women(person):
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def work(self):
        print "%sϲ������" %self.name
    def shopping(self):
        print "��%sϲ������" %self.name    

class man(person,women):
    def drink(self):
        print "��%s������ȶ���" %self.name

from person import *

person1=person("zhangsan",175,65)
person1.rest()
person1.work()

women1=women("lisi",172,62)
women1.work()
women1.rest()
women1.shopping()

man1=man("wangwu",171,61)
man1.work()
man1.drink()
man1.rest()
man1.shopping()

2.��鿴���´��룬����
class A:
   def go(self):
      print "go A go!"
   def stop(self):
      print "stop A stop!"

class B(A):
   def go(self):
      print "go B go!"

class C(A,B):
   def stop(self):
      print "stop C stop!"

ʵ�������£�
a=A();b=B();c=C()

�����н����
a.go();a.stop();    #go A go!    stop A stop!

b.go();b.stop();    #go B go!    stop A stop!

c.go();c.stop();    #go A go!    stop C stop!
