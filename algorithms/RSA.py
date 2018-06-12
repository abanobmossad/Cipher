from math import gcd
import random


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def inverse(E, Z):
    inx = [Z, E]
    mod = []
    last = [0, 1]
    try:
        i = 0
        while inx[-1] != 0:
            m = inx[i] // inx[i + 1]
            mod.append(m)
            inx.append(inx[i] % inx[i + 1])
            i += 1
    except Exception:
        print("There is no modular multiplicative inverse for this integer")
        return False

    mod.reverse()
    for i in range(1, len(mod)):
        try:
            l = (mod[i] * last[i]) + last[i - 1]
            last.append(l)
        except IndexError:
            pass

    # check the -1 or 1
    x1, x2 = inx[0], inx[1]
    y1, y2 = last[-1], last[-2]
    fun = x1 * y2 - y1 * x2
    if fun == 1:
        mmi = Z - last[-1]
    elif fun == -1:
        mmi = last[-1]
    else:
        print("There is no modular multiplicative inverse for this integer")
        return False
    return mmi


def generate_keys(p, q):

    if is_prime(p) and is_prime(q):
        n = p * q
        z = (p - 1) * (q - 1)
        e = random.randrange(1, z)

        while True:
            if gcd(e, z) == 1:
                break
            else:
                e = random.randrange(1, z)

        d = inverse(e, z)
        return e, d, n
    elif p == q:
        return False
    else:
        return False


# encryption uses (E,N) of the receiver
def encryption(plan_text, E, N,alpha):
    cipher_text = []
    for p in plan_text:
        c = (alpha.index(p) ** E) % N
        cipher_text.append(c)

    return cipher_text


# Decryption uses (D,N) of the receiver
def decryption(cipher_text, D, N,alpha):
    plan_text = []
    for c in cipher_text:
        p = (c ** D) % N
        p = alpha[p]
        plan_text.append(p)

    return "".join(plan_text)

def show():
    choose = input("Enter [[enc]/dec] :\n")
    if choose == 'enc':
        plan = input("Enter your plan text :\n")
        e, d, n = generate_keys(23, 87)
        print("This values  (E =", e, "D =", d, "N =", n, ") used for decryption\n")
        # apply encryption
        cc = encryption(plan_text=plan, E=e, N=n,alpha="")
        print("Cipher Text = ", cc)
    elif choose == "dec":
        cipher = []
        c = input("Enter your cipher text with separate \",\" ").split(',')
        for i in c:
            cipher.append(int(i))

        print(cipher)
        d = input('Enter The [D] and [N] values in order  with separate \",\" ').split(',')
        dec = []
        for i in d:
            dec.append(int(i))
        print(dec)
        # apply decryption
        dd = decryption(cipher, D=dec[0], N=dec[1])
        print("Plan Text = ", dd)

# show()