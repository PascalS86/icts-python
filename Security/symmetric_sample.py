def encode(n_key='', n_text=''):
    enc = []

    for i in range(len(n_text)):
        key = n_key[i % len(n_key)]
        cypher = (ord(n_text[i]) + ord(key)) % 256
        enc.append(chr((cypher)))
    return ''.join(enc)

def decode(n_key='', n_text=''):
    l = list(n_text)
    dec = []
    for i in range(len(n_text)):
        key = n_key[i % len(n_key)]
        decypher = chr((256 + ord(n_text[i]) - ord(key)) % 256)
        dec.append(decypher)
    return ''.join(dec)


e = encode(n_key='password', n_text='Hello World')
print(e)
print(decode(n_key='password', n_text=e))
