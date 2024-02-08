
#pyspellchecker library- a wrapper class around peter Norvig's famous spell checker algorithm
#pip install pyspellchecker


from spellchecker import SpellChecker

def spell_check(text):
    spell = SpellChecker()
    
    words = text.split()
    

    misspelled = []
    
    for word in words:
        if not spell.correction(word.lower()) == word.lower():
            misspelled.append((word, spell.correction(word.lower())))
    
    return misspelled

if __name__ == "__main__":
    input_text = input("Enter text to check spelling: ")
    
    misspelled_words = spell_check(input_text)
    
    if misspelled_words:
        print("Misspelled words and  suggestions:")
        for word, suggestion in misspelled_words:
            print(f"{word} -> {suggestion}")
    else:
        print("No misspelled words found.")
