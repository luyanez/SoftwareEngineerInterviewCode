def palindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left =left + 1
        right = right -1

    return True

pal = palindrome("abceocba")
print("The word is a palindrome: ",pal)