import sys

input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()

stack = []
lastchar = bomb[-1]
bombl = len(bomb)

for c in s:
    stack.append(c)
    if stack[-1] == lastchar and ''.join(stack[-bombl:]) == bomb:
        del stack[-bombl:]
answer = ''.join(stack)

if answer == "":
    print("FRULA")
else:
    print(answer)


# import sys

# input = sys.stdin.readline

# s = input().rstrip()
# bomb = input().rstrip()

# while True:
#     s = "".join(s.split(bomb))
#     if s.find(bomb) == -1:
#         break
# if s == "":
#     print("FRULA")
# else:
#     print(s)
    