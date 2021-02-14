logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def dyncrypt(direc,dstr,dshi):
    fstr = ""
    for num in range (len(dstr)):
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
