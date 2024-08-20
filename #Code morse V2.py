#Code morse V2

morsdict = {"a":"-o", "b": "-ooo"}
def morse (word):
    tot=""
    for letter in word:
        tot += morsdict[letter]+"/"
    return tot
print(morse("aba"))

