import sys

def numeral_to_chinese(numeral: type[int], lang = 'chs' or 'cht' or 'jps' or 'jps_daiji') -> str:
    '''
    Convert Arabic numerals into Chinese.\n
    将阿拉伯数字转换成中文大写。\n
    阿拉伯數字轉中文大寫。\n
    アラビア数字を漢数字に変換します。\n  
    'chs' for 中文大写, 'cht' for 中文大寫, 'jps' for 漢数字, 'jps_daiji' for 漢数字（大字）, default 'chs'.\n
    \n
    Example:
    >>> numeral_to_chinese(0)
    '零'
    >>> numeral_to_chinese(1234567809)
    '壹拾贰亿叁仟肆佰伍拾陆万柒仟捌佰零玖'
    >>> numeral_to_chinese(1002010)
    '壹佰万贰仟零壹拾'
    >>> numeral_to_chinese(1000000001)
    '壹拾亿零壹'
    >>> numeral_to_chinese(sys.maxsize)
    '玖佰贰拾贰亿亿叁仟叁佰柒拾贰万亿零叁佰陆拾捌亿伍仟肆佰柒拾柒万伍仟捌佰零柒'
    >>> numeral_to_chinese(300200600, lang = 'cht')
    '參億零貳拾萬零陸佰'
    >>> numeral_to_chinese(1050012140, lang = 'jps')
    '十億五千一万二千百四十'
    >>> numeral_to_chinese(900000000, lang = 'jps')
    '九億'
    >>> numeral_to_chinese(1050012340, lang = 'jps_daiji')
    '壱拾億五阡壱萬弐阡参佰四拾'
    '''
    assert sys.version_info >= (3, 0) #This function is writen in Python 3. Not sure if it's working in Python 2.
    assert type(numeral) is int #number must be int.
    assert numeral >= 0
    assert lang == 'chs' or lang == 'cht' or lang == 'jps' or lang == 'jps_daiji'
    
    def language_selecter(lang: str) -> list:
        if lang == 'chs':
            result = [{'0':'零', '1':'壹', '2':'贰', '3':'叁', '4':'肆', '5':'伍', '6':'陆', '7':'柒', '8':'捌', '9':'玖'}, 
                     ['', '拾', '佰', '仟'], 
                     ['万', '亿', '万亿', '亿亿']] #Add more if you feel necessary. But you have to change the variable(number) into string to support larger numeral.

        elif lang == 'cht':
            result = [{'0':'零', '1':'壹', '2':'貳', '3':'參', '4':'肆', '5':'伍', '6':'陸', '7':'柒', '8':'捌', '9':'玖'},
                      ['', '拾', '佰', '仟'], 
                      ['萬', '億', '兆', '京']]

        elif lang == 'jps':
            result = [{'0':'〇', '1':'一', '2':'二', '3':'三', '4':'四', '5':'五', '6':'六', '7':'七', '8':'八', '9':'九'},
                      ['', '十', '百', '千'], 
                      ['万', '億', '兆', '京']]

        else:
            result = [{'0':'〇', '1':'壱', '2':'弐', '3':'参', '4':'四', '5':'五', '6':'六', '7':'七', '8':'八', '9':'九'},
                      ['', '拾', '佰', '阡'], 
                      ['萬', '億', '兆', '京']]
    
        yield from result

    language = language_selecter(lang)
    s_dic_chinese = next(language)
    s_list_chinese = next(language)
    s_special_list_chinese = next(language) 
    
    def digits_generater(list) -> str:
        '''
        yield elements from list.
        >>> iter = digits_generater([1, 2])
        >>> next(iter)
        1
        >>> next(iter)
        2
        >>> next(iter)
        1
        '''
        while True:
            yield from list

    number = str(numeral)
    n = len(number)
    s_list = digits_generater(s_list_chinese)
    s_special_list = digits_generater(s_special_list_chinese)
    
    def convert_digits(number, count, n, zero_signal) -> str:
        '''Convert digits into chinese. However, the convertion has not been completed yet. Remove_unnecessary_digit function will cover the loose end'''
        digit = number[-1:]
        count += 1
        s = next(s_list)

        if n == 1:
            return s_dic_chinese[digit]

        if digit == '':
            return ''
        
        if count >= 5 and (count - 5) % 4 == 0:
            s_special = next(s_special_list)
            if digit == '0':
                if zero_signal == 1:
                    zero_signal = 0
                return convert_digits(number[:-1], count, n, zero_signal) + s_special
            zero_signal = 1
            return convert_digits(number[:-1], count, n, zero_signal) + s_dic_chinese[digit] + s_special

        if digit == '0':
            if zero_signal == 0:
                return convert_digits(number[:-1], count, n, zero_signal)
            zero_signal = 0
            return convert_digits(number[:-1], count, n, zero_signal) + s_dic_chinese[digit]
        zero_signal = 1
        return convert_digits(number[:-1], count, n, zero_signal) + s_dic_chinese[digit] + s

    def remove_unnecessay_digit(number, n) -> str:
        '''This function try to support really large number.
        If the number you need to convert is not that large, you can just hard code the replace_list such as ['億萬', '兆億', '京兆']'''
        if n > 1 and number[-1:] == '零':
            number = number[:-1]
        if n > 1 and lang == 'jps_daiji':
            number = number.replace('〇', '')
        elif n > 1 and lang == 'jps':
            number = number.replace('〇', '').replace('一十', '十').replace('一百', '百').replace('一千', '千')

        if n > 8:
            '''
            tmp1, tmp2, replace_list = [], [], []
            for i in s_special_list_chinese[1:]:
                tmp1.append(i)
            for i in s_special_list_chinese[:-1]:
                tmp2.append(i)
            for i in range(len(tmp1)):
                replace_list.append(tmp1[i] + tmp2[i])
            '''
            #Hard code the replace_list to speed up the function
            if lang == 'chs':
                replace_list = ['亿万', '万亿亿', '亿亿万亿']
            elif lang == 'jps':
                replace_list = ['億万', '兆億', '京兆']
            else:
                replace_list = ['億萬', '兆億', '京兆']
            for i in range(len(replace_list)):
                number = number.replace(replace_list[i], s_special_list_chinese[i + 1])
        return number

    return remove_unnecessay_digit(convert_digits(number, 0, n, 1), n)