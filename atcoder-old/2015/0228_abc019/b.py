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
S = input().rstrip()

E = run_length_encoding(S)

ans = ""
for char,cnt in E:
    ans += char + str(cnt)

print(ans)