# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = input().rstrip()

from collections import Counter
C = Counter(N).most_common()

print("SAME" if C[0][1] == 4 else "DIFFERENT")