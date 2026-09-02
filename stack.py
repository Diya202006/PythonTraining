stack = []
top = -1

def push(x, n):
    global top
    if top >= n-1:
        print("Stack Overflow")
    else:
        top += 1
        stack.append(x)

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
    else:
        print(stack.pop())
        top -= 1

def peek():
    if top == -1:
        print("Stack Underflow")
    else:
        print(stack[top])

def isEmpty():
    if top == -1:
        print("true")
    else:
        print("false")

n = int(input())
q = int(input())

for _ in range(q):
    cmd = input().split()
    if cmd[0] == "PUSH":
        push(int(cmd[1]), n)
    elif cmd[0] == "POP":
        pop()
    elif cmd[0] == "PEEK":
        peek()
    elif cmd[0] == "ISEMPTY":
        isEmpty()