import collections
def duplicate_count(text):
    return len({k:v for k,v in collections.Counter(text.lower()).items() if (v > 1 and k != ' ')})
text = "AaBbcc"
print(duplicate_count(text))