import sys


def inverseMod(h, alpha):
    for i in range(1, alpha):
        if (h * i) % alpha == 1:
            return i
    return None


def encryption(plan_text, a, s, alpha):
    cipher = []
    for char in plan_text:
        index = alpha.index(char)
        c = (a * index + s) % len(alpha)
        cipher.append(c)

    cipher_char = []
    for item in cipher:
        char = alpha[item]
        cipher_char.append(char)

    return ("".join(cipher_char))


def decryption(a, s, cipher_text, alpha):
    plain = []
    inverse = inverseMod(a, len(alpha))
    if inverse ==None:
        return False
    for char in cipher_text:
        index = alpha.index(char)
        c = inverse * (index - s) % len(alpha)
        plain.append(c)

    plain_char = []
    for item in plain:
        char = alpha[item]
        plain_char.append(char)

    return ("".join(plain_char))


# abcdefghijklmnopqrstuvwxyz fkfsxk
# ABCDEFGHIJKLMNOPQRSTUVWXYZ FKFSXK


#
# alpha=input("inter lenght of alphabitic")
# p= input("input your text to text")
# try:
#     for char in p:
#          if char not in alpha:
#              raise
# except:
#     print("your text use char you haven't")
#
# a = int(input("Input the amplitude : "))
# s = int(input("Input the shift : "))
# ss = encryption(p,a,s,alpha)
# print(ss)
# cc =decryption(a,s,ss,alpha)
# print(cc)
# if choose ==1:
#
#     for char in p:
#             index=alpha.index(char)
#             c=encryptchar(index,len(alpha))
#             cipher.append(c)
#     print("cipher text is: ")
#     for item in cipher:
#         char = alpha[item]
#         print(char, end='')
# else:
#     for char in p:
#         index = alpha.index(char)
#         c=decryptchar(index,len(alpha))
#         plain.append(c)
#
#     print("plain text is: ")
#     for item in plain:
#         char = alpha[item]
#         print(char, end='')
#

'''
import sys


def encryptchar(a,s,char,alpha):
    cipher = []
    return (a*char+s)%alpha

def decryptchar(a,s,char,alpha):
    inverse=inverseMod(a,alpha)
    return inverse*(char-s)%alpha
# abcdefghijklmnopqrstuvwxyz fkfsxk
# ABCDEFGHIJKLMNOPQRSTUVWXYZ FKFSXK
def inverseMod(h,alpha):
    for i in range(1,alpha):
        if ( h*i ) % alpha == 1:
            return i
    return None


# alpha=input("inter lenght of alphabitic")
# p= input("input your text to text")
# try:
#     for char in p:
#          if char not in alpha:
#              raise Exception
# except Exception:
#     print("your text use char you haven't")
#     sys.exit()

def kk(plan_text,a,s,alpha):
    cipher = []
    for char in plan_text:
        index = alpha.index(char)
        c = encryptchar(a,s,index, len(alpha))
        cipher.append(c)
    print("cipher text is: ")
    for item in cipher:
        char = alpha[item]
        print(char, end='')

    return cipher
def dd(a,s,cipher_text,alpha):
    plain = []
    for char in cipher_text:
        index = alpha.index(char)
        c = decryptchar(a,s,index, len(alpha))
        plain.append(c)

    print("plain text is: ")
    for item in plain:
        char = alpha[item]
        print(char, end='')

'''
