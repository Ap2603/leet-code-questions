def isAnagram(self, s: str, t: str) -> bool:
    sdict = dict()
    tdict = dict()

    for char in s:
        if char in sdict:
            sdict[char] += 1
        else:
            sdict[char] = 1
    for char in t:
        if char in tdict:
            tdict[char] += 1
        else:
            tdict[char] = 1
    return sdict == tdict

