def solution(s):
    l = len(s)
    final = []
    for i in range(l):
        c = s[i]
        if 'a' <= c <= 'z':
            pos = ord(c) - ord('a')
            final.append(chr(ord('a') + 25 - pos))
        else:
            final.append(c)
    return ''.join(final)