# 1525
# O(N)

def numsplit(s):
    n = len(s)
    prefix = [0]*n
    suffix = [0]*n
    view = set()
    ans = 0
    for i in range(n):
        view.add(s[i])
        prefix[i] = len(view)

    view.clear()
    for i in reversed(range(n)):
        view.add(s[i])
        suffix[i] = len(view)

    for i in range(n-1):
        if prefix[i] == suffix[i+1]:
            ans += 1

    return ans
