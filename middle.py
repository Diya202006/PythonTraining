def get_middle(s):
    n = len(s)

    if n % 2 == 1:
        return s[n // 2]
    else:
        return s[n // 2 - 1] + s[n // 2]


if _name_ == "_main_":
    word = input().strip()
    print(get_middle(word))