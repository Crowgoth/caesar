#!/usr/bin/python3

def create_alpha_strings(shift):
    # accepts integer for shifting the alphabet
    # return a regular alphabet string and a shifted one.
    alpha_string ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_string = alpha_string[shift:26] + alpha_string[0:shift]
    return alpha_string, cipher_string

# -------------------------------------------------------------------

def encrypt_char(character, alpha_string, cipher_string):
    # accepts a cleartext character, regular alphabet and the shifted one
    # returns the encrypted character
    index = alpha_string.find(character)
    output = cipher_string[index]
    return output

def encrypt_string(message, alpha_string, cipher_string):
    # remove all non-alpha-characters from cleartext
    # returns the encrypted string
    message = message.upper()
    encrypted_string=""
    for c in message:
        if c.isalpha():
            encrypted_string = encrypted_string + encrypt_char(c, alpha_string, cipher_string)
    return encrypted_string

# -----------------------------------------------------------------

def decrypt_char(character, alpha_string, cipher_string):
    # accepts an encrypted character, regular alphabet and a shifted one.
    # returns cleartext character
    index = cipher_string.find(character)
    output = alpha_string[index]
    return output

def decrypt_string(message, alpha_string, cipher_string):
    # takes the encrypted string, the regular and the shifted alphabet-string
    # returns the decrypted string
    message = message.upper()
    decrypted_string = ""
    for c in message:
        if c.isalpha():
            decrypted_string = decrypted_string + decrypt_char(c, alpha_string, cipher_string)
    return decrypted_string

# -------------------------------------------------------------------

def main():
    shift = input("How many characters should the alphabet be shifted (1-25): ")
    shift = int(shift)
    alpha_string, cipher_string = create_alpha_strings(shift)
    print(f"Alphabet:         {alpha_string}")
    print(f"Shifted alphabet: {cipher_string}\n")

    choice = ""
    processed_message = ""
    while not (choice =="e" or choice == "d"):
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? ")
    message = input("\nPlease enter message: ")
    if choice =="e":
        processed_message = encrypt_string(message, alpha_string, cipher_string)
    if choice == "d":
        processed_message = decrypt_string(message, alpha_string, cipher_string)
    print(f"Processed message: {processed_message}") 



if __name__ == "__main__":
    main()



