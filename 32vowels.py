# vowel or consonant
vowels = ['a','e','i','o','u']
alph_input = input("Enter an alphabet: ")
if alph_input.isalpha():
    if alph_input in vowels:
        print("Vowel")
    else:
        print("Consonant")