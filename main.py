from func import dyncrypt , logo

print (logo)

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")

if direction == "e":
    text = input("\nType your message to encrypt :\n").lower()
    shift = int(input("\nType the shift number : \n"))
    dyncrypt(direc=direction,dstr=text,dshi=shift)
elif direction == "d":
    text = input("\nType your message to dycrypt :\n").lower()
    shift = int(input("\nType the shift number : \n"))
    dyncrypt(direc=direction,dstr=text,dshi=shift)
else:
    print(f"you gave wrong direction {direction}")









# if direction == "e":
#     text = input("\nType your message to encrypt :\n").lower()
#     shift = int(input("\nType the shift number : \n"))
#     encrypt(estr=text,nshi=shift)

# elif direction == "d":
#     text = input("\nType your message to decrypt :\n").lower()
#     shift = int(input("\nType the shift number : \n"))
#     decrypt(sstr=text,sshi=shift)
# else:
#     print(f"you gave wrong direction {direction}")