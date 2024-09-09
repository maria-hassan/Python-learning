def palindrome(s1):
    return s1 == s1[::-1]


s = "madam"
r = palindrome(s)


def check(result):
    if result:
        print(True)
    else:
        print(False)


check(r)
