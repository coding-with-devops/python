
def update(word):
    with open("content.txt", "r") as fh:
        words = fh.read()
    new_word = words.replace(word, "######")
    if word in words:
        with open("content.txt", "w") as fh:
            fh.write(new_word)
    print(words)

word1 = "donkey"
update(word1)