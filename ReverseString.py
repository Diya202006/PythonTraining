stack = []

def push(ch):
    stack.append(ch)

def pop():
    if len(stack) == 0:
        return ""
    return stack.pop()

def reverse_string(s):
    # Push each character
    for ch in s:
        push(ch)
    
    # Pop characters to form reversed string
    result = ""
    while len(stack) > 0:
        result += pop()
    
    return result

s = input()
print(reverse_string(s))