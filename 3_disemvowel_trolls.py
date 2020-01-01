vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
def disemvowel(string):
    for vowel_letter in vowels:
        string = string.replace(vowel_letter, "") 
    return string
string = "Mike is a python noob"
print(disemvowel(string))
        
    
    # return for word in string

# return s.translate(None, "aeiouAEIOU")

# return "".join(c for c in string if c.lower() not in "aeiou")