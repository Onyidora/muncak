# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
     
    # the sorted strings are checked
    if(sorted(word)== sorted (anagram)):
        print("True")
    else:
        print("False")        
         
# driver code1 
word ="hello"
anagram ="check"
find_anagram(word,  anagram)
    
# driver code2 
word ="below"
anagram ="elbow"
find_anagram(word,  anagram)
    

