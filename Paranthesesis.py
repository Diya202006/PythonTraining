stack = []

def push(ch):
    stack.append(ch)

def pop():
    if len(stack) == 0:
        return None
    return stack.pop()

def is_matching(open_br, close_br):
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    return pairs.get(open_br) == close_br

def is_balanced(expr):
    for ch in expr:
        if ch in "({[":
            push(ch)
        elif ch in ")}]":
            if len(stack) == 0:
                return False
            
            open_br = pop()
            if not is_matching(open_br, ch):
                return False
    
    return len(stack) == 0

s = input()
print("Balanced" if is_balanced(s) else "Not Balanced")