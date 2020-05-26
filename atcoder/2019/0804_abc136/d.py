# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def run_length_encoding(String):
    s = String
    cnt = 1
    Res = []
    try:
        for i in range(len(s)):
            if s[i] == s[i+1]:
                cnt += 1
            else:
                Res.append((s[i],cnt))
                cnt = 1
    except:
        Res.append((s[i],cnt))
    return Res


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
S = input().rstrip() + "x"

E = run_length_encoding(S)

Ans = []
for i in range(len(E)//2):
    R = E[i*2][1]
    L = E[i*2+1][1]
    for r in range(R-1):
        Ans.append(0)
    x,y = R//2+L//2, R//2+L//2
    if R%2 == 1:
        x += 1
    if L%2 == 1:
        y += 1
    Ans.append(x)
    Ans.append(y)
    for l in range(L-1):
        Ans.append(0)

print(*Ans)