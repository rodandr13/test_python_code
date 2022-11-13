def generate_numbers(N, M, prefix=None):
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()


def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    for digit in "01":
        gen_bin(M-1, prefix + digit)


gen_bin(3)
# generate_numbers(10, 3)
