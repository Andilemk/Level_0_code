def vowel_detector(word):
    list_of_vowels = ["a","e","i","o","u"]
    word = word.lower()
    vowels = ""
    for letter in list_of_vowels:
        if letter in word and letter not in vowels:
            vowels += letter + ", "
    print(f"Vowels: {vowels}")
    
vowel_detector("Omnicron")
    
    

    
    
    
    
    
    
    
    
    
    
