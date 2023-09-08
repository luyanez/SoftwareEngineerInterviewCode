def make_the_string_great(s):
    stack = []
    for curr_char in s:
        if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(curr_char)

    return ''.join(stack)

s = "abBAcC"
ans = make_the_string_great(s)
print("The good string: ",ans)