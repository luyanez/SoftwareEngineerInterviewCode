def sentence_panagram(sentence):
    letters = set(sentence)
    if len(letters) == 26:
        return True
    return False

sentence = "thequickbrownfoxjumpsoverthelazydog"
ans = sentence_panagram(sentence)
print("Is this sentece a panagram: ",ans)