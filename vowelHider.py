def hide_vowels(s):
    result = ""

    for ch in s:
        if ch in "aeiouAEIOU":
            result += "*"
        else:
            result += ch

    return result


if __name__ == "__main__":
    word = input().strip()
    print(hide_vowels(word))