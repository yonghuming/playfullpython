import codecs
import random
from functools import reduce

# 经过山东菏泽王晓辉老师的提醒
# 随机名称还可以用汉字区位码
# 改进程序

# 知乎得到启发
# str = "\"\\u5c3c\\u5eb7\""
# str = codecs.decode(str,'unicode_escape')
# print(str)  #输出：尼康

def random_char():
    # Unicode统一汉字编码范围
    # 从统一编码范围里找出汉字
    char_code = random.randint(0x4e00, 0x9fbb)
    str = "\\u{}".format(format(char_code, 'x'))
    char = codecs.decode(str,'unicode_escape')
    # 根据得到的范围数字得到汉字
    return char

def random_gb2312_char():
    char_code = random.randint(0xb0a1, 0xd7ff)
    str = "\\u{}".format(format(char_code, 'x'))
    char = codecs.decode(str,'gb2312')
    # 根据得到的范围数字得到汉字
    return char
# 并非常用汉字范围，常用汉字没有特定的区间
# 需要自行排出
# 所以找出常用字然后随机生成也是个办法了
# 至于那种方便就很难说了
def cre_name():
    username = ['', '', '']
    name = map(lambda x : x + random_char(), username)
    username = ''.join(list(name))
    return username

print(cre_name())

for x in range(10):
    print(cre_name())
# 进一步改进是找到常用汉字的编码
# 或者不用Unicode码而用表示汉字比较少的编码
