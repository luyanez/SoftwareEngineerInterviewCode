def is_subsequence(str1, str2):
    pointer1 = 0
    pointer2 = 0

    while pointer1 < len(str1) and pointer2 < len(str2):
        if str1[pointer1] == str2[pointer2]:
            pointer1 += 1
        pointer2 += 1

    return pointer1 == len(str1)



str1 = "ace"
str2 = "abcde" #"aec"
res = is_subsequence(str1, str2)
print("String 2 is subsequence of Str1: ",res)