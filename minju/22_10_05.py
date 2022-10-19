import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(n, arr, visited):
    visited[n] = True
    for i in arr[n]:
        if not visited[i]:
            dfs(i, arr, visited)

            
n, m = map(int, input().split())
arr = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i, arr, visited)
        count+=1
print(count)