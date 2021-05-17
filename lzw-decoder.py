import argparse
import os
import pickle


def decompression (lines):
    DictionarySize = 256
    dictionary = {} #store the dictionary
    result = [] # stores the uncompressed result

    #initializing dictionary with ASCII table
    for i in range (0, DictionarySize):
        dictionary[i] = str(chr(i)) 

    previous = chr(lines[0]) 
    lines = lines[1:] #removes the first character from the entry
    result.append(previous) #add the first character to the result

    for bit in lines:
        aux = ""
        if bit in dictionary.keys ():
            aux = dictionary[bit] #patch the character corresponding to the bit in the dictionary
        else: #When the bit is not in the dictionary, it should be taken
            aux = previous + previous[0] 
            
                
        result.append (aux) #add to result
        #Simulating how substrings were added during compression
        dictionary[DictionarySize] = previous + aux[0] 
        DictionarySize += 1 #Increment dictionary size
        previous = aux #previous receives the current character
        
    return result


content=pickle.load(open("naman.bin","rb"))
result=decompression(content)

output=open("namandecode.txt","w")

for l in result:
    output.write(l)
output.close()



