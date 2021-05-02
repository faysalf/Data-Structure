def super_reduced_string(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    if len(stack)==0:
        return "Empty String"
    return ''.join(stack)

if __name__ == "__main__":
    s = input()
    print(super_reduced_string(s))