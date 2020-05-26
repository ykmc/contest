# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())

len1 = [0]*(N)
for i in range(N-1):
    print("? {} {}".format(i+1,N))
    sys.stdout.flush()
    len1[i] = int(input())

k = len1.index(max(len1))

len2 = [0]*N
for i in range(N):
    if i != k:
        print("? {} {}".format(i+1,k+1))
        sys.stdout.flush()
        len2[i] = int(input())

print("! {}".format(max(len2)))
