COSC326 Etude 3: Joined Up Writing

Authors: Markham Meredith, Ollie Whiteman.

Program that takes two words to find singly and doubly links for and a dictionary of words to try and find links in.

2 words "Join up" if a proper suffix of one is a proper prefix of another, e.g. Suffix and Fixture. The common part can be singly or doubly joined.

Singly joined: common parts is at least half as long as one of two words
Doubly Joined: common part is at least half as long as both words.


To run the code, in the command line of terminal cd to the folder containing the ogmain.py file. Run the command "python ogmain.py" followed by the 2 words you want to find links between then a "<" to the path containing the dictionary you wish to test on.

An example: "python ogmain.py a bb < dict2.txt"
or "python ogmain.py a bb < /JoinedUp/dictionaries/dict2.txt"

The output of this code is 2 lines. The first line contains the numebr of singly linked words if any, followed by the chain of words. The second line is the amount of doubly linked words followed by the chain. 

