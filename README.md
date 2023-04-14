# numeral_to_Chinese

Convert Arabic numerals into Chinese.  
阿拉伯数字转换成中文大写。  
阿拉伯數字轉中文大寫。  
アラビア数字を漢数字に変換します。  

## Hello world!
I guess this is my 'Hello World!'. For the first time I write a python program for my own. Only wrote code in excel using VBA before.

## Example
```
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
```
