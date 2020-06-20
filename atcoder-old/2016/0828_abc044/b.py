# python 3.4.3
import sys
input = sys.stdin.readline
# import numpy as np
from collections import Counter

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
W = input().rstrip()

C = Counter(W).most_common()

ans = "Yes"
for _,cnt in C:
    if cnt%2 == 1:
        ans = "No"
        break

print(ans)