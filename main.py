# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Emiya

from my_01_class import MyClass

me = MyClass()

if me.sex == '男':
    print('My name is %s,I am a boy' % me.name)
elif me.sex == '女':
    print('My name is %s,I am a girl' % me.name)
else:
    print('My name is %s,秀吉的性别就是秀吉啊' % me.name)


me.work()
me.study()
