def remove_adjacent_duplicates_string(s):
    stack = []

    for value in s:
        if stack and stack[-1] == value:
            stack.pop()
        else:
            stack.append(value)
        
    return ''.join(stack)

s = "abbaca"
ans = remove_adjacent_duplicates_string(s)
print("The final string without duplicates is: ",ans)