from itertools import combinations

n = int(input())
arr = []

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

nums = [i for i in range(1, n+1)]
combi = list(combinations(nums, n//2))

first = []
second = []

for i in combi[:len(combi)//2]:
    count = 0
    for j in combinations(i, 2):
        count += arr[j[0]-1][j[1]-1]
        count += arr[j[1]-1][j[0]-1]
    first.append(count)

for i in combi[len(combi)//2:]:
    count = 0
    for j in combinations(i, 2):
        count += arr[j[0]-1][j[1]-1]
        count += arr[j[1]-1][j[0]-1]
    second.append(count)

first.reverse() 
sub = 1000
for i, j in zip(first, second):
    sub = min(sub, abs(i-j))
print(sub)
