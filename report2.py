import string

upperLetter = string.ascii_uppercase
s = input().upper()
code = list(set(upperLetter)-set(s))
code.sort()
ls = list(set(s))
ls.sort(key = s.index)
keys = ''.join(ls + code)
decode = input().upper()
table = ''.maketrans(upperLetter, keys)
print(decode.translate(table))