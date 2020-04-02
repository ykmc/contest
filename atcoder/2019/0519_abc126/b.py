import sys
input = sys.stdin.readline

S = int(input())

s1 = S//100
s2 = S%100

yymm = 1<=s2<=12
mmyy = 1<=s1<=12

ans = ""
if yymm:
    if mmyy:
        ans = "AMBIGUOUS"
    else:
        ans = "YYMM"
else:
    if mmyy:
        ans = "MMYY"
    else:
        ans = "NA"

print(ans)