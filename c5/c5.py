import binascii

stanza = b'''Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal'''
key = b'ICE'

outstr = bytearray()
for i, byte in enumerate(stanza):
    outstr.append(byte ^ key[i%3])

print(binascii.hexlify(outstr))
