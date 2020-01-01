# function to flip reverse letters in words of a length of 5 letters or greater
def spin_words(sentence):
    wordlist = sentence.split()
    for word in wordlist:
        if len(word) >= 5:
            result += (word[::-1] + " ")
        else:
            result += (word + " ")
    return result.strip()
# driver code and result
sentence = "Testing big words and small"
result = spin_words(sentence)
print(result)

# add one liner