from func import dyncrypt , logo

print (logo)

runtime = True

while runtime == True:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    text = input("\nType your message :\n").lower()
    shift = int(input("\nType the shift number : \n"))
    if direction == "e":
        dyncrypt(direc=direction,dstr=text,dshi=shift)
    elif direction == "d":
        dyncrypt(direc=direction,dstr=text,dshi=shift)
    else:
        print(f"you gave wrong direction {direction}")

    want = input("type y to continue. n to exit.")

    if want == "n":
        runtime = False



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