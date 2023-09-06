def valid_parenthesis(s):
    matching = {"(":")","[":"]","{":"}"}
    stack = []

    for value in s:
        if value in matching:
            stack.append(value)
        else:
            if not stack:
                return False
            closing = stack.pop()
            if matching[closing] != value:
                return False
                 
    return not stack

s = "({})"
ans = valid_parenthesis(s)
print("Valid parenthesis? ",ans)