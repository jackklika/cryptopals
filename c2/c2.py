ex1 = bytearray.fromhex("1c0111001f010100061a024b53535009181c")
ex2 = bytearray.fromhex("686974207468652062756c6c277320657965")

outlist = []
for i, n in enumerate(ex1):
    outlist.append(hex(ex1[i] ^ ex2[i]))

print(outlist)
