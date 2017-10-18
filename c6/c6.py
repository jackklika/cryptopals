from base64 import *
def hammingdist(s1, s2):
    d = 0
    for a, b in zip(s1, s2):
        distance = a^b # Distance between ascii byte vals

        # For each byte in the difference, count the 1s
        for bit in bin(distance): 
            if bit == '1': d += 1 
    return(d)

breakme = b64decode(open('c6.txt', 'rb').read())

print(breakme)

sizearr = []
for size in range(2,40):
    dist = hammingdist(breakme[0:size], breakme[size:size*2])
    print(dist/size)
    sizearr.append([size, dist/size])

likelysize = min(sizearr, key=lambda x:x[0])
