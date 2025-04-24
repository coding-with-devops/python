
strg = "\n You are amazing.."

with open("this.txt", "a") as fh:
    fh.write(strg)
with open("this.txt", "r") as f:
#    print(f.read())
    #fh = f.readlines()
     fh = f.readlines()
print(fh)

