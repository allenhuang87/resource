#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def f(x, y):
        return x * y
    return reduce(f, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
 
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解

import math
def quadratic(a, b, c):
    m=b*b-4*a*c
    if m>=0:
        x=(-b+math.sqrt(m))/(2*a)
        y=(-b-math.sqrt(m))/(2*a)
        return x,y
    else:
        return 'no answer!'

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    while(s[:1]==' '):
        s=s[1:]
    while(s[-1:] == ' '):
        s = s[:-1]
    return s
