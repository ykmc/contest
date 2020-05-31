# PyPy3 (2.4.0)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
from collections import defaultdict, deque
class DAG:
    def __init__(self, adjList, inDegreeArray):
        self.A = adjList
        self.In = inDegreeArray
        self.n = len(inDegreeArray)
        self.depth = [-1]*(self.n)
        self.nodes = []

    def sort(self):
        dq = deque()
        # 入次数が 0 の頂点を deque に入れる
        for i in range(self.n):
            if self.In[i] == 0:
                dq.append(i)
                self.depth[i] = 0
        while dq:
            v1 = dq.popleft()
            self.nodes.append(v1)
            for v2 in self.A[v1]:
                self.In[v2] -= 1
                self.depth[v2] = max(self.depth[v2], self.depth[v1] + 1)
                if In[v2] == 0:
                    dq.append(v2)
    
    def get_node_array(self):
        if len(self.nodes) == self.n:
            return self.nodes
        else:
            return []
    
    def get_depth(self):
        if len(self.depth) == self.n:
            return self.depth
        else:
            return []

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

# 試合と頂点の対応表
M = [[-1 for _ in range(N)] for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(i+1,N):
        M[i][j] = cnt
        M[j][i] = cnt
        cnt += 1

# 試合 j が 試合 i の翌日以降にしか行えない -> G[i][j]

G = [[] for _ in range((N*(N-1)//2))]
# 頂点(試合) の入次数
In = [0]*(N*(N-1)//2)
# 入力からグラフ, 配列を生成
for i in range(N):
    for j in range(N-2):
        gagem_id = M[i][ A[i][j] - 1 ]
        next_game_id = M[i][ A[i][j+1] - 1 ]
        G[gagem_id].append(next_game_id)
        In[next_game_id] += 1

dag = DAG(G, In)
dag.sort()
node = dag.get_node_array()
depth = dag.get_depth()

if len(node) == 0:
    print(-1)
else:
    print(max(depth) + 1)