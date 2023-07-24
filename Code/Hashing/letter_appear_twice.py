def letter_appear_twice(letters):
    seen = set()
    for c in letters:
        if c in seen:
            return c
        seen.add(c)

letters = "abcdeda"
ans = letter_appear_twice(letters)
print("The first letter to appear twice is: ",ans)