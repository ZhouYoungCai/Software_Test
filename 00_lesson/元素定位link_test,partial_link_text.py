UI���Ľ����Զ�������Ҫ��������������

1.��Ŀ�����㹻��
2.����ִ�еĹ���
3.��Ŀ����
4.�����ȶ�
#coding:utf-8
from selenium import webdriver
from time import *
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("https://www.baidu.com/")
# bro.find_element_by_link_text("����").click() #link_text�ǶԳ����ӵ�������о�ȷƥ�䶨λԪ��
sleep(1)
bro.find_element_by_partial_link_text("��").click() #partial_link_text�ǶԳ����ӵ��������ģ��ƥ�䶨λԪ��
