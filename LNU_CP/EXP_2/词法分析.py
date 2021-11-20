'''
功能：基于python-lex的词法分析器
Made by @JessyTsui 2020/10/20

*实现思路*
  三步走：1.定义tokens 2.对每个token定义正则表达式 3.输入字符串，调用lex构建分析器

*接口说明*
  - getToken() : 获取下一个token
  返回值：LexToken(str type, repr value, int lineno, int lexpos)
        词法对象的参数依次为：类型，值，行号，在字符串中的偏移（从1开始）

*参考文档*
  - English：http://www.dabeaz.com/ply/ply.html
  - Chinese：https://www.cnblogs.com/P_Chou/p/python-lex-yacc.html

'''

import ply.lex as lex
tokens = [
    # 算数运算符
    'add', 'sub', 'mul', 'div',
    # 关系运算符
    'less', 'greater', 'unequal', 'equal', 'notless', 'notgreater',
    # 赋值运算符
    'assignment',
    # 界符
    'bracel', 'bracer', 'parenl', 'parenr', 'bracketl', 'bracketr', 'comma', 'semi', 'annotation',
    # 常量
    'NUMINT', 'NUMFLOAT',
    # 标识符
    'ID',
    # 换行符
    'LF',
    'tab'
]

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'void': 'VOID',
    'while': 'WHILE',
    'int': 'INT',
    'float': 'FLOAT'
}

tokens += reserved.values()

# 以下为各个token的正则表达式定义，采用 t_tokenName 的命名方式
t_ignore = r'[ ]+'

# 关系、算术运算符
t_unequal = r'!='
t_notless = r'>='
t_notgreater = r'<='
t_equal = r"=="

t_add = r'\+'
t_sub = r'-'
t_mul = r'\*'
t_div = r'/'
t_less = r'<'
t_greater = r'>'
t_assignment = r'='

# 界符
t_bracel = r'{'
t_bracer = r'}'
t_parenl = r'\('
t_parenr = r'\)'
t_bracketl = r'\['
t_bracketr = r'\]'
t_comma = r','
t_semi = r';'

# 忽略注释
def t_annotation(t):
    r'(/\*(.|\n)*?\*/)|(\/\/.*)'  # 第一行写正则表达式
    t.lexer.lineno += t.value.count('\n')  # 累计行数
    pass  # 表示忽略该token


# 忽略换行
def t_LF(t):
    r'[ ]+\n'
    pass


# 忽略tab
def t_tab(t):
    r'\t'
    pass


# 识别数字
def t_NUMINT(t):
    r'[0-9]+'
    t.value = int(t.value)  # 返回时字符串类型，需转为整型
    return t


def t_NUMFLOAT(t):
    r'[0-9]*\.?[0-9]+$'
    t.value = float(t.value)  # 返回时字符串类型，需转为float型
    return t


# 识别标识符
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


# 增加行数
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  # 计算行数


# 错误处理：输出错误符号，行数，列数后跳过当前错误继续扫描
def t_error(t):
    # print("Illegal character '%s'" % t.value[0], "(%d," % t.lexer.lineno, "%d)" % t.lexer.lexpos)
    tmp = t.lexpos - data.rfind('\n', 0, t.lexpos)
    print(f"========Illegal character: {t.value[0]}   line: {str(t.lineno)}   col: {str(tmp)}")
    t.lexer.skip(1)  # 跳过当前字符

# 调用Lex模块，构建词法分析器
lexer = lex.lex()

# 测试输入文件与结果输出文件
f = open('./test', 'r', encoding='UTF-8')
data = f.read()
f1 = open('output.txt', 'w')
lexer.input(data)

ISTEST = True  # 打开测试
# ISTEST = False # 关闭测试
if ISTEST:
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
        tok = str(tok)
        f1.write(tok)
        f1.write("\n")


# =============================================================================
#  获取Token的接口
# =============================================================================
def getToken():
    return lexer.token()


# 文件流关闭
f.close()
f1.close()