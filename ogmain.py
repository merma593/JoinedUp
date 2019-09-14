'''
COSC326 Etude 3 Joined Up Writing
Authors: Markham Meredith, Ollie Whiteman

A program which finds singly and doubly linked between 2 words from,
command line and prints the amount of links followed by the word chain
'''


import sys
import fileinput
import queue




def doublematch(word1, word2):
    # Finds & Compares suffix and prefix of 2 words
    # Checks if doubly linked
    prefix = word1
    suffix = word2
    preLen = len(word1)
    sufLen = len(word2)

    if(preLen > sufLen):
        prefix = prefix[preLen - sufLen:]
    elif(preLen < sufLen):
        suffix = suffix[:preLen]
            
    while(suffix != prefix and len(suffix) > 0):           
        prefix = prefix[1:]
        suffix = suffix[:len(suffix) - 1]

    if(prefix == suffix):
        if(len(prefix) < (preLen)/2 or len(prefix) < (sufLen)/2):
            return False
        return True

        
        


def singlematch(word1, word2):
    #Finds & compares suffix and prefix of 2 words
    #Checks if singly linked
    prefix = word1
    suffix = word2
    preLen = len(word1)
    sufLen = len(word2)
    if(preLen > sufLen):
        prefix = prefix[preLen - sufLen:]
    elif(preLen < sufLen):
        suffix = suffix[:preLen]
            
    while(suffix != prefix and len(suffix) > 0):           
        prefix = prefix[1:]
        suffix = suffix[:len(suffix) - 1]

    if(prefix == suffix):
        if(len(prefix) < (preLen)/2 and len(prefix) < (sufLen)/2):
            return False
        return True





if __name__ == "__main__":
    
    words = sys.argv[1:]
    first = words[0]
    second = words[1]
    dictionary = sys.stdin.read().splitlines()
    wordqueue = queue.Queue()
    wordqueue.put(first)
    matchWords = []
    visitedWords = set()
    result = ""
    word2 = []

    if first in dictionary and second in dictionary and first != second:
        
        while wordqueue.empty() == False and second not in matchWords:
            
            word = wordqueue.get()
            word2 = word.split()
            for words in dictionary:
                if singlematch(word2[-1], words) == True and words != word:
                    matchWords.append(words)
  
        
            for elem in matchWords:
                if elem == second:
                    result = word + " " + elem
                elif elem not in visitedWords:
                    wordqueue.put(word + " " +elem)
                    visitedWords.add(elem)
        print(len(result.split()), result)
        
        
        matchWords = []
        visitedWords = set()
        result = ""
        wordqueue = queue.Queue()
        wordqueue.put(first)
 

        while wordqueue.empty() == False and second not in matchWords:
            
            word = wordqueue.get()
            word2 = word.split()
            for words in dictionary:
                if doublematch(word2[-1], words) == True and words != word:
                    matchWords.append(words)
                    
            
            for elem in matchWords:
                if elem == second:
                    result = word + " " + elem
                elif elem not in visitedWords:
                    wordqueue.put(word + " " +elem)
                    visitedWords.add(elem)
        print(len(result.split()), result)



    
    elif first in dictionary and second in dictionary and first == second:
        print("1", first)
        print("1", first)
    else:
        print("Words not in dictionary!")




    
         
    
    
