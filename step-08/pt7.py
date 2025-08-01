# write a python function to remove a given word from list ad strip it as the same time
def rem(l, word):
    n = []
    for item in l:

        if not (item == word):
          n.append(item.strip(word))
    return n


l = ["Ayush", "apdan", "Krishan", "an"]
print(rem(l, "an"))
