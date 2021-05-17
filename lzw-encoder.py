import pickle
import argparse
import os

def compression(lines):
    DictionarySize = 256
    dictionary = {} #store the dictionary
    result = [] # stores the compressed result
    temp = "" # variable that will store the substrings
    
    #Adding ASCII table to the dictionary
    for i in range (0, DictionarySize):
        dictionary [str(chr(i))] = i #How is the dictionary {'a': 97, 'b': 98}
    #so we can browse the file, and replace the substrings with their respective integers
    
    
    for c in lines: #Find the file
        
        temp2 = temp + str(chr(c)) # temp2 receives the current character plus the previous one to check if it exists in the dictionary
        if temp2 in dictionary.keys (): #if it is in the dictionary temp = temp2 to be concatenated later with the next character
            temp = temp2
        else: #when temp2 content is not in the dictionary
            result.append (dictionary[temp]) # we take the integer that represents the previous string in the dictionary and add it to the result
            dictionary [temp2] = DictionarySize # then we add temp2 to the dictionary
            DictionarySize += 1 #Increment dictionary size
            temp = "" + str (chr(c)) #reset the variable with the current substring

    if temp!= "": # if the temporary string is not empty, add to the result
        result.append(dictionary[temp]) #picking the integer that represents it in the dictionary
        
    return result

text=open("naman.txt","rb").read()
result=compression(text)

output=open("naman.bin","wb")

pickle.dump (result, output) #writes the compression file in binary

output.close()





