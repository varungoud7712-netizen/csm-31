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


def dfs():
    stack = [[(8, 0, 0)]]
    visited = set()

    while stack:
        path = stack.pop()
        s = path[-1]

        if s in visited:
            continue
        visited.add(s)

        if target in s:
            for x in path:
                print(x)
            return

        for n in next_states(s):
            if n not in visited:
                stack.append(path + [n])


dfs()
