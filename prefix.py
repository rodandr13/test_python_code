"""
Быстрый способ вычисления префикса строки
"""


def prefix(s):
    v = [0] * len(s)
    for i in range(1, len(s)):
        k = v[i-1]
        while k > 0 and s[i] != s[k]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v


if __name__ == "__main__":
    string = "abcdabcabcdabcdab"
    print(prefix(string))
