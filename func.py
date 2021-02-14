alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(estr,nshi):
    sstr = ""
    for num in range (len(estr)):
        letter = estr[num]
        lsn = alphabet.index(letter) + nshi
        lspos= 0
        if lsn >= len(alphabet):
            lspos = (lsn % len(alphabet))
        elif lsn >= len(alphabet):
            lspos = (lsn % len(alphabet))
        else:
            lspos = lsn
        sstr += alphabet[lspos]
    print(sstr)



def decrypt(sstr,sshi):
    rstr = ""
    for num in range (len(sstr)):
        letter = sstr[num]
        lsn = alphabet.index(letter) - sshi
        lspos= 0
        if lsn < 0:
            lspos = (lsn % len(alphabet))
        elif lsn >= len(alphabet):
            lspos = (lsn % len(alphabet))
        else:
            lspos = lsn
        rstr += alphabet[lspos]
    print(rstr)
