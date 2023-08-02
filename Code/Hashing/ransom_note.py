from collections import Counter

def ransom_note(ransomNote, magazine):

    magazine_counts = Counter(magazine)
    ransom_note_counts = Counter(ransomNote)
    
    # For each *unique* character in the ransom note:
    for char, count in ransom_note_counts.items():
        # Check that the count of char in the magazine is equal
        # or higher than the count in the ransom note.
        magazine_count = magazine_counts[char]
        if magazine_count < count:
            return False

    
    return True


ransomNote = "ab"
magazine = "aab"
ans = ransom_note(ransomNote, magazine)
print("Can we create the ransom note with the magazine provided? :",ans)



