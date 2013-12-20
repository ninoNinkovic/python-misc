def piglatin_ize(s):
    """Translates an English word into Pig Latin."""
 
    # Initial lists and strings
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U", "y", "Y"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    consonant_string = ""
 #separate the input s to swich vowels and consonats for pig latin expressions
    s = s.split()
    for k, word in enumerate(s):
        consonant_string = "" 
        for i in vowels:
            if word[0] == i:
                word =(word + "way")
                #s[k] = word
                #word[0]=str(word)
                break
 
        for x in range(len(word)):
            if word[x] in vowels:
                break
            for i in consonants:
                if word[x] == i:
                    consonant_string += i
        word = word[len(consonant_string):]
        word += consonant_string
        word += "ay"
        s[k] = word
#retruns the string s pinglatinized!
##    for e in range(len(s)):
##        if s[e]==" ":
##            " " =="-"
##            print s
        for a in s:
##            if s[a]==" ":
##                " " = "-"
                print a,
                return  word

print piglatin_ize("hello world")

