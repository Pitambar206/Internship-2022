# Both players are given the same string,S .
#Both players have to make substrings using the letters of the string S.
#Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
#The game ends when both players have made all possible substrings.
#Scoring
#A player gets +1 point for each occurrence of the substring in the string S.

def minion_game(string):
    k=0
    s=0
    vowels="AaEeIiOoUu"
    for i in range(len(string)):
        if string[i] in vowels:
            k=k+len(string)-i
        else:
            s=s+len(string)-i    
    
    if k>s:
        print("Kevin",k)
    elif k==s:
        print("Draw")    
    else:
        print("Stuart",s)            

if __name__ == '__main__':
    s = input()
    minion_game(s)