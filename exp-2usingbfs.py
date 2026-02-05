from collections import deque

cap = (8, 5, 3)
target = 7

def next_states(s):
    res = set()
    for i in range(3):
        for j in range(3):
            if i != j:
                a = list(s)
                t = min(a[i], cap[j] - a[j])
                a[i] -= t
                a[j] += t
                res.add(tuple(a))
    return res

q = deque([[(8,0,0)]])
vis = {(8,0,0)}

while q:
    path = q.popleft()
    s = path[-1]

    if target in s:
        for x in path:
            print(x)
        break

    for n in next_states(s):
        if n not in vis:
            vis.add(n)
            q.append(path + [n])
