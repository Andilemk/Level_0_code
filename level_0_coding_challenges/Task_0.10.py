def common_letters(string1, string2):
    common_char = ''
    for letter in string2:
        if letter in string1:
            common_char += letter + ","
            
    print(f"Common letters: {common_char}")
    
common_letters("Njabulo", "Khumalo")
            