import collections
def duplicate_encode(word):
    characters = [letter for letter in word.lower()]
    duplcount = (collections.Counter(characters))
    return ''.join([')' if duplcount[char] > 1 else '(' for char in characters])
word = "Philanthropy"
print(duplicate_encode(word))
