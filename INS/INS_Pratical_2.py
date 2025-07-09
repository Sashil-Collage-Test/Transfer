def columnar_encrypt(plaintext,key):
    col=len(key)
    row=(len(plaintext)+col-1)//col

    plaintext+='_'*(row*col-len(plaintext))

    matrix=[list(plaintext[i*col:(i+1)*col]) for i in range(row)]

    ciphertext=""
    for k in key:
        ciphertext+="".join([matrix[i][k] for i in range (row)])
    return ciphertext

def columnar_decrypt(ciphertext,key):
    col=len(key)
    row=(len(ciphertext)+col-1)//col

    matrix=[[""]*col for _ in range(row)]
    index=0
    for k in range(col):
             col_index=key.index(k)
             for i in range(row):
                 if index<len(ciphertext):
                     matrix[i][col_index]=ciphertext[index]
                     index+=1
                     
    plaintext="".join(["".join(row) for row in matrix])
    return plaintext.replace('_','')

def main():
    plaintext="HELLO"
    key=[1,0,3,2]

    ciphertext=columnar_encrypt(plaintext,key)
    print("Encrypted message:",ciphertext)

    decrypted_text=columnar_decrypt(ciphertext,key)
    print("Decrypted message:",decrypted_text)

if __name__== "__main__":
    main()


