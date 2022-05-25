def common_letters(string1, string2):
    common_char = ''
    string1 = string1.lower()
    string2 = string2.lower()
    for letter in string2:
        if letter in string1 and letter not in common_char:
            common_char += letter + ","
    common_char = common_char.rstrip(",")
    print(f"Common letters: {common_char}")
    
common_letters("Njabulo", "nnJhumalo")
            
