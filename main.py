from func import encrypt , decrypt

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")


if direction == "e":
    text = input("Type your message to encrypt :\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(estr=text,nshi=shift)

elif direction == "d":
    text = input("Type your message to decrypt :\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(sstr=text,sshi=shift)
else:
    print(f"you gave wrong direction {direction}")