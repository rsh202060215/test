# Name Hong
# Time 2021/3/15 1:15
# Pro  生成一系列算术式
'''
第一步 ：输入生成的式子个数
第二步 ：生成随机数和运算符号
第三步 ：计算并验证
第四部 : 保存到文本中
'''

import random
import operator

op = ('+', '-', '×', '÷')
equation = []


# 进行计算
def cal(op, x, y):
    if op == 0:
        return x + y
    elif op == 1:
        return x - y
    elif op == 2:
        return x * y
    else:
        return x / y


# 检查重复
def check(a, b, c, i, j):
    for x in equation:
        if x == [a, b, c, i, j]:
            return 0
    return 1


k = 0
n = 5  # 产生公式的个数
m = 0  # 用来计数，一共有多少公式
while True:
    try:
        n = int(input('请输入产生公式的个数'))
    except ValueError:
        print('本次输入无效，请输入数字')
    else:
        break

# 将数据输出到文件当中，注意1、所指定的盘符存在，2 使用file = fp  相当于文件描述符
# fp = open('D:/subject.txt', 'a+')  # a+如果文件不存在就创建，存在就在文件内容的后面继续追加
fp = open('./subject.txt', 'w')  # w 在当前目录下创建文件，并覆盖原文件内容
while k <= n:
    a = random.randint(0, 100)  # 用来产生三个0-100的整数
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    i = random.randint(0, 3)  # 用来产生两个运算符
    j = random.randint(0, 3)
    m+=1
    if ((i == 3) & (b == 0)) | ((j == 3) & (c == 0)):  # 避免被除数为0
        continue
    if j > 1:
        result = cal(j, b, c)
        if (i == 3) & (result == 0):  # 避免被除数为0
            continue
        result = cal(i, a, result)
    else:
        result = cal(i, a, b)
        result = cal(j, result, c)
        # print(type(result))   调试时使用
    if (result < 0) | (result > 100) :
        continue
    if (check(a, b, c, i, j) == 1) & (type(result) == int):
        equation.append([a, b, c, i, j])
        str = "%3d %s %3d %s %3d\t= %3d" % (a, op[i], b, op[j], c, result)
        print(str)   # 调试时使用
        print(str, file=fp)
        k = k + 1
    else:
        continue
print('公式产生完成,一共尝试%d次' % m)
fp.close()
