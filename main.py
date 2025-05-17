#!/usr/bin/python3

def create_alpha_strings(shift):
    # accepts integer for shifting the alphabet
    # return a regular alphabet string and a shifted one.
    alpha_string ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_string = alpha_string
    cipher_string = cipher_string[shift:26] + cipher_string[0:shift]
    return alpha_string, cipher_string


def encrypt_char(character, alpha_string, cipher_string):
    # accepts a cleartext character, regular alphabet and the shifted one
    # returns the encrypted character
    index = alpha_string.find(character)
    output = cipher_string[index]
    return output


def decrypt_char(character, alpha_string, cipher_string):
    # accepts an encrypted character, regular alphabet and a shifted one.
    # returns cleartext character
    index = cipher_string.find(character)
    output = alpha_string[i]
    return output


def main():
    shift = input("How many characters should the alphabet be shifted (1-25): ")
    shift = int(shift)
    alpha_string, cipher_string = create_alpha_strings(shift)
    print(f"Alphabet:         {alpha_string}")
    print(f"Shifted alphabet: {cipher_string}\n")
    cleartext = input("Please enter cleartext: ")
    cleartext = cleartext.upper()
    cipher =""
    for c in cleartext:
        cipher = cipher + encrypt_char(c, alpha_string, cipher_string)
    print(f"Ciphertext: {cipher}")


if __name__ == "__main__":
    main()



