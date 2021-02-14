alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    sstr = ""
    for num in range (len(text)):
        letter = text[num]
        lsn = alphabet.index(letter) + shift
        lspos= 0
        if lsn >= len(alphabet):
            lspos = (lsn % len(alphabet))
        else:
            lspos = lsn
        sstr += alphabet[lspos]
    print(sstr)


encrypt(text= text,shift=shift)

# sstr = ""
# for num in range (len(text)):
#     letter = text[num]
#     lsn = alphabet.index(letter) + shift
#     lspos= 0
#     if lsn >= len(alphabet):
#         lspos = (lsn - len(alphabet))
#     else:
#         lspos = lsn
#     sstr += alphabet[lspos]
# print(f"{sstr}")



# # #=========================
# slist=[]
# sstr = ""
# for num in range (len(string)):
#     letter = string[num]
#     # takes letter of input string
#     # slist.append(letter)
#     # puts that letter in slist list
#     lspos = alphabet.index(letter) + nshift
#     # lspos = alphabet.index(slist[num]) + nshift
#     # finds position of that letter in alphabet
#     # slist[num] = alphabet[lspos]
#     sstr +=alphabet[lspos]
#     # print (slist)
#     # sstr += slist[num]

# print(sstr)



# # ================================
# string = "hello"
# nshift = 1
# # lshift = ""
# print (string)
# si = []
# ss = []

# for i in string:
#     si.append(alphabet.index(i)+nshift)

# print (si)

# for i in si:
#     ss.append(alphabet[i])
    
# sstring = ""

# for i in ss:
#     sstring += i

# print (ss)

# print(sstring)
## ============================



















# def encrypt():
#     print("hello")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 