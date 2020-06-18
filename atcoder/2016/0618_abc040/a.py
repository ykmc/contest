# Python3 (3.8.2)
import sys
input = sys.stdin.readline

N,X = map(int,input().split())
 
print(min(X-1,N-X))