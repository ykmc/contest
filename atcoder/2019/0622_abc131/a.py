# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
S = input().rstrip()

ans = "Good"
for i in range(len(S)-1):
    if S[i]==S[i+1]:
        ans = "Bad"

print(ans)