filename = "CIH Bilingual Medical Glossary English-Spanish.txt"

file = open(filename)
text = file.read()


text.replace("."," ")
text.replace(","," ")
text.replace("-"," ")
text.replace(":"," ")
text.replace("/"," ")
text.replace("'"," ")
text.replace("("," ")
text.replace(")"," ")
text.replace(";"," ")

text = text.lower()

tokens = text.split()

def check_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

def find_anagrams(words):

    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    return anagrams

resultado = find_anagrams(tokens)
for key, value in resultado.items():
    print(f'{key}: {value}')
    

