# PyPy3 (2.4.0)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def matrix_prod(m1,m2):
    h = len(m1)
    w = len(m2[0])
    m2trans = list(zip(*m2))
    ret = [[None]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            v = 0
            for a,b in zip(m1[y],m2trans[x]):
                v ^= (a&b)
            ret[y][x] = v
    return ret
 
def matrix_pow(X,n):
    ret = None
    mag = X
    while n > 0:
        if n & 1:
            ret = mag if ret is None else matrix_prod(mag, ret)
        mag = matrix_prod(mag, mag)
        n >>= 1
    return ret

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
K,M = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

if M<=K:
    print(A[M-1])
    sys.exit()

#
# | C1 C2  ...  Ck-1 Ck | | An+k-1 |   | An+k   |
# |  1  0  ...     0  0 | | An+k-2 |   | An+k-1 |
# |  0  1  ...     0  0 | | An+k-3 | = | An+k-2 |
# |                     | |        |   |        |
# |  0  0  ...     1  0 | | An     |   | An+1   |
#
X = [[0 for _ in range(K)] for _ in range(K)]
for i in range(K):
    X[0][i] = C[i]
for i in range(K-1):
    X[i+1][i] = (1<<32)-1 # 積の単位元, 今回は and なので全bitが1の数値を使う

mat = matrix_pow(X, M-K)
ans = matrix_prod(mat, [[a] for a in A[::-1]])
print(ans[0][0])