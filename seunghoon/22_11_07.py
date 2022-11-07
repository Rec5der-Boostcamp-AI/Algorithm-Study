# wider93 님 코드 : 112 ms (python3)
# combinations, zip 활용
'''
import sys
from itertools import combinations as cb

N = int(sys.stdin.readline()) // 2
M = 2 * N

stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
allstat = sum(newstat) // 2

mins = 65535
for l in cb(newstat[:-1], N):
    mins = min(mins, abs(allstat - sum(l)))
print(mins)
'''


# my : 1248 ms (python3)
# itertools combination
'''
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
weight_l = [list(map(int, input().split())) for _ in range(n)]
weight_d = dict(((i, j), weight_l[i - 1][j - 1] + weight_l[j - 1][i - 1]) for i, j in combinations(range(1, n + 1), 2))

min_i = 10000
synergy_l = [sum(weight_d[tup] for tup in combinations(team, 2)) for team in combinations(range(1, n + 1), n // 2)]

i, j = 0, len(synergy_l) - 1
while i < j:
    min_i = min(min_i, abs(synergy_l[i] - synergy_l[j]))
    i += 1
    j -= 1

print(min_i)
'''


# my : 2476 ms (python3)
# dfs, stack
'''
import sys
input = sys.stdin.readline


def dfs(depth: int) -> None:
    global diff, start, link

    if not depth:
        return
    if depth == N>>1:
        diff = min(diff, abs(start-link))
        return

    for i in range(s_stack[-1]+1, N):
        for k in s_stack:
            start += scores[i][k] + scores[k][i]
        for k in l_set:
            link -= scores[i][k] + scores[k][i]
        
        s_stack.append(i)
        l_set.remove(i)
        dfs(depth+1)
        l_set.add(s_stack.pop())

        for k in s_stack:
            start -= scores[i][k] + scores[k][i]
        for k in l_set:
            link += scores[i][k] + scores[k][i]
    return


if __name__ == '__main__':
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    start = 0; link = sum(sum(line[1:]) for line in scores[1:])
    diff = 20_000
    s_stack = [0]
    l_set = {i for i in range(1, N)}
    dfs(1)
    print(diff)
'''