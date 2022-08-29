# 49 Group Anagrams
#   O(n * m)


def groupAnagrams(strs):
   # res = {}
    res = defaultdict(list)
    # to avoid edge case of its not dict
    for s in strs:
        count = [0]*26

        for c in s:
            count[ord(c)-ord("a")] += 1

        res[tuple(count)].append(s)  # as list cannot be keys

    return res.values()
