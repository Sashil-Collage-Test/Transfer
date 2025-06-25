def caesar_encrypt(plaintext,shift):
    ciphertext= ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset=65 if char.isupper()else 97
            ciphertext+=chr((ord(char)-ascii_offset+shift)%26+ascii_offset)
        else:
            ciphertext+=char
    return ciphertext

def caesar_decrypt(ciphertext,shift):
    return caesar_encrypt(ciphertext,-shift)

def main():
    plaintext=input("Enter the message:")
    shift=int(input("Enter the shift value:"))

    ciphertext=caesar_encrypt(plaintext,shift)
    print("Encrypted message:",ciphertext)

    decrypted_text=caesar_decrypt(ciphertext,shift)
    print("Decrypted message:",decrypted_text)

if __name__== "__main__":
    main()
