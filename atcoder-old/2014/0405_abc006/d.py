# Python3 (3.4.3)
import sys
input = sys.stdin.readline
import bisect

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
class LIS():
    def __init__(self, a):
        self.lis = [a[0]]
        for i in range(len(a)):
            if a[i] > self.lis[-1]:
                self.lis.append(a[i])
            else:
                self.lis[bisect.bisect_left(self.lis, a[i])] = a[i]
    
    def get(self):
        return self.lis


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())g
C = [int(input()) for _ in range(N)]

L = LIS(C)
lis = L.get()

print(N-len(lis))