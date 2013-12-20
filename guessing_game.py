print "Think of a number from 1 to 100"
smallest=1
largest=100
answer=" "
while answer!= "equal":
    guess=(smallest+largest)/2
    answer= raw_input("Is your number 'more', 'less' or ' equal' to " +str(guess) + " ?")
    if answer == "more":        
        smallest= guess +1
    elif answer== "less":
        largest= guess -1
                
                
    print smallest, largest
print"I got it!!"
