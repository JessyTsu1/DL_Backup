# coding:utf-8
"""
输出结果为'（关键词对应的序号，关键词）
例如输入为：
if(y=1)
    else x=1
    while(达维) 王昊=1；
    return 0;
输出为：
(2,if) (27,() (10,'y') (25,=) (11,1) (28,)) (10,'else') (10,'x') (25,=) (11,1) (4,while) (27,() (10,'达维') (28,)) (10,'王昊') (25,=) (11,1) (29,return) (11,0) (26,;)
Made by @Jessy 2020/10/18
"""
#关键字字典，一个关键词匹配一个数字
dic = {'begin': 1, 'if': 2, 'then': 3, 'while': 4, 'do': 5, 'end': 6,
              '+': 13, '-': 14, '*': 15, '/': 16, ':': 25, ':=': 18,
              '<': 20, '<>': 21, '<+': 22, '>': 23, '>=': 24, '=': 25,
              ';': 26, '(': 27, ')': 28, 'return': 29, '#': 0}

def emit(value, type_str):
    emit_index = ''
    emit_value = value
    if type_str == 'num':
        emit_index = '11'
    elif type_str == 'word':
        if value in dic.keys():
            emit_index = str(dic[value])
        else:
            emit_index = '10'
            emit_value = '\'' + value + '\''
    elif type_str == 'symbol':
        emit_index = str(dic[value])
    print('(' + emit_index + ',' + emit_value + ')', end=' ')


def lex(input_str):
    i = 0
    while input_str[i] != '#':
        char = input_str[i]

        if char == ' ' or char == '\t' or char == '\n':
            pass

        elif char.isdigit():
            num_str = char
            while input_str[i + 1].isdigit():
                i += 1
                num_str += input_str[i]
            emit(num_str, 'num')

        elif char.isalpha():
            word_str = char
            while input_str[i + 1].isalnum():
                i += 1
                word_str += input_str[i]
            emit(word_str, 'word')

        elif char in dic.keys():
            symbol_str = char
            while input_str[i + 1] in dic.keys():
                i += 1
                symbol_str += input_str[i]
            emit(symbol_str, 'symbol')
        i += 1
    emit('#', 'symbol')

if __name__ == '__main__':
    with open('code.txt', 'r', encoding='utf-8') as f:
        input_str = f.read()
        lex(input_str)