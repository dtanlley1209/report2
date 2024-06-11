# 南華大學Python程式設計-加密字符串-期末報告
11124127 王星圍 11124130 邱述陽
# 生成大寫英文字母的序列
```
import string 

upperLetter = string.ascii_uppercase
```
# 使用者輸入英文字串轉換成大寫
```
s = input().upper()
```
# 創建一個列表 code，其中包含了不在輸入字串 s 中的大寫英文字母，按順序排列
```
code = list(set(upperLetter)-set(s))
code.sort()
```
# 創建一個列表 ls，其中包含了輸入字串中不重複的字母，進行排序，排序是根據字母在原始輸入字串中的順序
```
ls = list(set(s))
ls.sort(key = s.index)
```
# 將列表 ls 和 code 組合成一個新的字串，並賦值給變數 keys ，將新字串用作替換密碼表。
```
keys = ''.join(ls + code)
```
# 使用者輸入須加密的字串轉換成大寫，建立一個轉換表 table，用於將須加密的字串替換為替換密碼表中對應的字母。
```
decode = input().upper()
table = ''.maketrans(upperLetter, keys)
print(decode.translate(table))
```
