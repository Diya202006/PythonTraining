stack = []

def push(x):
    stack.append(x)

def peek():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print(stack[-1])

n = int(input())

if n == 0:
    print("Stack Underflow")
else:
    elements = list(map(int, input().split()))
    
    for x in elements:
        push(x)
    
    peek()