#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
words = {
    "namaskar": "Hello",
    "dhanyabad": "Thank you",
    "subh din": "Good morning",
    "subh ratri": "Good night",
    "krupaya": "Please",    
}

input_word = input("Enter a Hindi word to look up its English translation: ") 
print(words.get(input_word, "Word not found!"))

if input_word in words:
    print(f"The English translation of '{input_word}' is '{words[input_word]}'")
else:
    print("Word not found!")    