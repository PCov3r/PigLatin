#----------------------------------------------------------------------------
# Created By    : PCov3r
# Created Date  : 11/11/2022
# version ='1.1'
# ---------------------------------------------------------------------------
# This python program can be used to turn any string containing a
# passage of English language text into its Pig Latin translation. 
# The result is printed out.
# The string is first split into words, punctuation and whitespaces.
# Then each word is transformed to its Pig Latin equivalent.
# Finally, each word that began with a capital letter is recapitalized,
# and the final sentence is assembled by concatenating each word.
# ---------------------------------------------------------------------------


VOWELS = ['a','e','i','o','u']

## Split a string (including punctuation marks and whitespaces).
## Takes a string s in input and return a list of words and ponctuations.
def full_split(s):
    word = ""
    sentence = []
    for char in s : 
        if(char.isalpha()):  # Char is a letter
            word += char  # Add to word buffer
        else: # Char is not a letter
            if(word != ""):  # Word is not empty, append to sentence
                sentence.append(word) 
            sentence.append(char)  # Append punctuation
            word = ""
    if(word != ""):  # Empty word buffer
            sentence.append(word)
    return sentence 

## Extract and return the position of the first vowel in a word. 
## Returns -1 if the word is a whitespace or ponctuation mark.
def find_first_vowel(word):
    if(not word.isalpha()):  # word is a ponctuation mark, 
        return -1            # whitespace or number
    for i, char in enumerate(word): 
        if(char in VOWELS):  # Char is a vowel
            return i
    return len(word)  # Word is only made of consonants

## Transform a word to its Pig Latin equivalent.
## Returns the Pig Latin word as a string.
def transform_word(word):
    word = word.lower() 
    idx = find_first_vowel(word)
    if(idx == 0):  # Word begins with a vowel
        return word + 'way'
    elif(idx>0):  # Word begins with a consunant
        return word[idx:] + word[:idx]+'ay'
    else:  # Word is a punctuation mark or whitespace
        return word


## Translate a string to Pig Latin and print the translation.
def pig_latin(s):
    pig_latin_s = ""
    translated_w = ""
    is_upper = False

    words = full_split(s)

    for word in words: 
        is_upper = word[0].isupper()  # Has a capital letter
        translated_w = transform_word(word)  # Transform to pig latin
        if(is_upper):
            pig_latin_s += translated_w.capitalize()
        else:
            pig_latin_s += translated_w
    return(pig_latin_s)
