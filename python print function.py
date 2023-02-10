# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

name='sambhu'
n=7


#style c
print('hello %(name)s%(number)dd' %{'name': name, "number": n})
print('hello %s%dd' %(name,n))
print(f'Hello {name}{n}d')



#style visual studio
print('Hello {}{}d'.format(name, n))

#print('{} Number=  {:2.2%}'.format(name, n))
#here {:2,2%} represent the output formating for the value which will be put there 
#here n which is assigned as 7
#since formated as {:2.2%} it will display 700%.00%


#style Java
print("Hello "+name+str(n)+'d')

#python style
print("Hello ",name,n,'d',sep='')




