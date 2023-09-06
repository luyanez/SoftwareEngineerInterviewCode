def backspace_string_compare(s,t):
    stack = []
    
    for value in s:
        if value != '#':
            stack.append(value)
        else:
            stack.pop()
    
    string1 = ''.join(stack)
    stack = []

    for value in t:
        if value != '#':
            stack.append(value)
        else:
            stack.pop()
    
    string2 = ''.join(stack)

    return string1 == string2

s = "ab#c"
t = "ad#c"
ans = backspace_string_compare(s,t)
print("Are the 2 strings equal after erasing the backspace character?: ",ans)