# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
W = input().rstrip()
 
ans = ""
for w in W:
    if w not in "aiueo":
        ans += w
 
print(ans)