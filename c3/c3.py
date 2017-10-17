import csv
# Import the letter frequencies as a dictionary (mapping characters to their frequencies)
# ie freqdict["a"] should return 11.682
def freq(ch):
    with open('../letterfreq.csv', mode='r') as infile:
        reader = csv.reader(infile)
        freqdict = {rows[0]:rows[1] for rows in reader}
    ch = ch.lower()
    try:
        freqdict[ch]
    except: 
        return 0.001
    return freqdict[ch]




def breakxor(ba):
    breaklist = []
    for char in range(ord('A'), ord('Z')+1):
        buildstring = ""
        for byte in ba:
            buildstring += chr(char ^ byte)
        breaklist.append(buildstring) 

    returnlist = []
    for astr in breaklist:
       monad = [] 
       monad.append(astr)
       monad.append(scorestring(astr))
       returnlist.append(monad)
    return max(returnlist, key=lambda x:x[1])

def scorestring(astr):
    score = 1
    for c in astr:
        score *= float(freq(c))
    return score

if __name__ == '__main__':
    challenge = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    print(breakxor(challenge))
