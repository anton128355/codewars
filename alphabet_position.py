# Replace With Alphabet Position
def alphabet_position(text):
    d = {x: y for x, y in list(zip('abcdefghijklmnopqrstuvwxyz', range(1, 28)))}
    return " ".join([" ".join([str(d[j]) for j in i if j in d ]) for i in text.lower().split()])