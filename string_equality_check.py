def string_equality_check(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True


if __name__ == "__main__":
    str1 = "String"
    str2 = "String"
    print(string_equality_check(str1, str2))
