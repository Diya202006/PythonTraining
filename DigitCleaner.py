def extract_digits(s):
    result = ""

    for ch in s:
        if ch.isdigit():
            result += ch

    return result


if __name__ == "__main__":
    word = input().strip()
    print(extract_digits(word))