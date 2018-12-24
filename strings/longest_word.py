def LongestWord(sen):

    words  = "".join([",",c][int(c.isalnum())] for c in sen).split(",")
    maxLen = max( [len(w) for w in words] )
    return [ w for w in words if len(w) == maxLen][0]
    
# keep this function call here  
print(LongestWord(raw_input()))