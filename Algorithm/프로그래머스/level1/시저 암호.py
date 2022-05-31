# 시저 암호
cng_ord = ""
s = "a B z"
n = 4
for alpa in list(s):
  if alpa != " ":
        ans = ord(alpa) - 64
        ans += n
        c = chr(ans + 64)
        cng_ord +=c
  else:
    cng_ord += ' '

cng_ord