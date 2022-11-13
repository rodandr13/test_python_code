def find(number, A):
    flag = False
    for x in A:
        if number == x:
            flag == True
            break
    return flag


def generate_permutations(N, M=-1, prefix=None):
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()


generate_permutations(3)