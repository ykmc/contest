# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
S = input().rstrip()
T = input().rstrip()

is_win = True

N = len(S)
for i in range(N):
    if S[i]=="@" and T[i]=="@":
        continue
    if S[i]=="@":
        if T[i] not in "atcoder":
            is_win = False
            break
    elif T[i]=="@":
        if S[i] not in "atcoder":
            is_win = False
            break
    else:
        if S[i] != T[i]:
            is_win = False
            break

print("You can win" if is_win else "You will lose")