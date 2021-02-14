logo = """ 
 ________  ___  ________  ___  ___  _______   ________     
|\   ____\|\  \|\   __  \|\  \|\  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \ \  \|\  \ \  \\\  \ \   __/|\ \  \|\  \   
 \ \  \    \ \  \ \   ____\ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \____\ \  \ \  \___|\ \  \ \  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \__\ \__\    \ \__\ \__\ \_______\ \__\\ _\ 
    \|_______|\|__|\|__|     \|__|\|__|\|_______|\|__|\|__|
                                                           
                                                           
                                                           

"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def dyncrypt(direc,dstr,dshi):
    fstr = ""
    for num in range (len(dstr)):
        if  dstr[num] in alphabet:
            letter = dstr[num]
            if direc == "e":
                work = "encoded"
                lsn = alphabet.index(letter) + dshi
            elif direc == "d":
                lsn = alphabet.index(letter) - dshi
                work = "decoded"
            lspos= 0
            if lsn < 0:
                lspos = (lsn % len(alphabet))
            elif lsn >= len(alphabet):
                lspos = (lsn % len(alphabet))
            else:
                lspos = lsn
            fstr += alphabet[lspos]
        else:
            fstr += dstr[num]
    print(f"\nThe {work} text is \n\n{fstr}\n")



# def encrypt(estr,nshi):
#     sstr = ""
#     for num in range (len(estr)):
#         letter = estr[num]
#         lsn = alphabet.index(letter) + nshi
#         lspos= 0
#         if lsn >= len(alphabet):
#             lspos = (lsn % len(alphabet))
#         elif lsn >= len(alphabet):
#             lspos = (lsn % len(alphabet))
#         else:
#             lspos = lsn
#         sstr += alphabet[lspos]
#     print(f"\nThe encoded text is \n\n{sstr}\n")



# def decrypt(sstr,sshi):
#     rstr = ""
#     for num in range (len(sstr)):
#         letter = sstr[num]
#         lsn = alphabet.index(letter) - sshi
#         lspos= 0
#         if lsn < 0:
#             lspos = (lsn % len(alphabet))
#         elif lsn >= len(alphabet):
#             lspos = (lsn % len(alphabet))
#         else:
#             lspos = lsn
#         rstr += alphabet[lspos]
#     print(f"\nThe encoded text is \n\n{rstr}\n")
