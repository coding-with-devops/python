censor_word = [ "donkey", "animal", "humans", "farmers"]

with open("content2.txt", "r") as fh:
    content = fh.read()

for word in censor_word:
    content = content.replace(word, "#" * len(word))
with open("content2.txt", "w") as fh:
        fh.write(content)
