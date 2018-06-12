import numpy as np

# this method take a string (key or [plain_text]) and make sorted table of it
append_chars_caps = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
append_chars_lower = list("abcdefghijklmnopqrstuvwxyz")


def convert_to_table(key='', plain_text=""):
    # figure the plain text type [lower , upper] case to append chars of his type
    if plain_text.islower():
        lower = True
    else:
        lower = False
    # remove the spaces from the plain text
    plain_text = plain_text.replace(" ", "")

    # setup the vars for quick edit
    key = list(key)
    plain_text = list(plain_text)
    plain_len = len(plain_text)
    key_len = len(key)

    # calculate the number of the remain chars
    append_number = key_len - (plain_len % key_len)
    if lower:
        split = append_chars_lower[0:append_number]
    else:
        split = append_chars_caps[0:append_number]
    # append the remaining chars to the table
    for i in split:
        plain_text.append(i)

    # adding the chars table
    table = []
    for i in range(0, plain_len, key_len):
        p_char = plain_text[i:i + key_len]
        table.append(p_char)

    # make the table a numpy array to easy access
    table = np.array(table)
    # print(table)

    # sort the key to needed for encrypt
    key.sort()
    sorted_key = key

    return table, sorted_key


# this method take the key and the plain text in numpy array form

def encryption(key, plain_text):
    # take the table and the sorted key from [convert_to_table] into vars
    table, sorted_key = convert_to_table(key, plain_text)
    # prepare the key
    print(sorted_key)
    key = list(key)
    # look into the table and return the encrypted words in sorted order
    encrypted_word_list = []
    for i in sorted_key:
        print(i)
        if sorted_key.index(i)== sorted_key.index(i)+1:
                indx =  key.index(i)+1
        else:
            indx = key.index(i)
        #     print(list(table[:, key.index(i)+1]))
        # print(list(table[:, key.index(i)]))
        encrypted_word_list.append(list(table[:, indx]))

    # convert every word from a list to string for representation
    cipher_text = []
    for i in encrypted_word_list:
        cipher_text.append("".join(i))

    return ("".join(cipher_text)),table


def decryption(key, cipher_text):
    # setup list to easy handle
    sorted_key = list(key)
    key = list(key)
    sorted_key.sort()
    cipher_text = list(cipher_text)
    column_length = int(len(cipher_text) / len(key))
    # slicing the cipher text to groups  according to [column_length]
    cipher_slicing = []
    for i in range(0, len(cipher_text), column_length):
        c_char = cipher_text[i:i + column_length]
        cipher_slicing.append(c_char)

    # make an empty table to inject the chars to is
    table = np.zeros((column_length, len(key))).astype(np.str)
    for i in range(column_length):
        for x in range(len(key)):
            table[i][x] = cipher_slicing[x][i]

    # reorganize the table depending on the key
    decrypted_word_list = []
    for i in key:
        decrypted_word_list.append(list(table[:, sorted_key.index(i)]))

    # make the table a numpy array to easy access
    decrypted_word_list = np.array(decrypted_word_list)
    # convert every word from a list to string for representation
    plan_text = []
    for i in range(decrypted_word_list.shape[1]):
        plan_text.append("".join(decrypted_word_list[:, i]))

    return ("".join(plan_text)),table


# this for chick if their are frequented chars in the key [chars in the key should be unique] for no conflict
def unique_chars_set(s):
    return len(s) == len(set(s))


# expected output for [NEWEROENBMWDDOCWONESA] "WE NEED MORE SNOW NOW"

# prompt flexible strings
def show():
    try:
        choose = str(input("Enter [[enc],dec] :\n"))
        if choose == "enc":
            plan = str(input("Enter your plain text : \n"))
            key = str(input("Enter your key word :  \n"))

            # check key word uniqueness
            if unique_chars_set(key):
                cipher_text = encryption(key, plan)
                print("Cipher text  = ", cipher_text)
            else:
                print("chars in the key should be unique for avoid conflict ")

        elif choose == "dec":
            cipher = str(input("Enter your cipher text : \n"))
            key = str(input("Enter your key word:  \n"))

            # check key word uniqueness
            if unique_chars_set(key):
                plan_text = decryption(key, cipher)
                print("Plan text = ", plan_text)
                print("\n*Since the matrix doesn’t hold spaces you’ll have to realize the text meaning your self")
                print("for example !!")
                print(plan_text.upper(),"with letters [ABCD]  doesn’t hold meaning so that must have")
                print("completed missing cells")
            else:
                print("chars in the key should be unique for avoid conflict ")

    except ValueError:
        print("please enter a string value")
