1. ����һ��ģ��person������һ��people�࣬
������������name�����height������weight ��
�෽��������work����Ϣrest��
���� women�̳�people�࣬
��д����:�����������µķ������
�ټ���һ������man��ͬʱ�̳�people����women�࣬
����������ˮ��
����һ���µ�ģ��dyp����person�е������࣬
����������ֱ���ж��󴴽������ø���������з�����
#coding:utf-8
class people:
    def __init__(self,name,sg,tz):
        self.name = name
        self.sg = sg
        self.tz = tz
    def work(self):
        print "��%sҪȥ������" %self.name
    def xiuxi(self):
        print "��%sҪȥ��Ϣ��" %self.name

class women(people):
    def work(self):
        print "��%s�Ǹ���ͥ��Ů���ڼҴ�С��" %self.name
    def gouwu(self):
        print "�ҵ������%2.2f,�ҵ�������%d,��%sҪȥ��������," %(self.sg,self.tz,self.name)

class man(people,women):
    def drink(self):
        print "�Ҳ�����ֻ���ˮ���һ��Ṥ����������Ϣ�����Ṻ��"

#coding:utf-8
from person import *
people1 = people("Tom",192.2,70)
people1.work()
people1.xiuxi()
print people1.name
women1 = women("Jan",188.3,100)
women1.work()
women1.xiuxi()
women1.gouwu()
man1 = man("�����",160.2,90)
man1.work()
man1.xiuxi()
man1.gouwu()
man1.drink()
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
