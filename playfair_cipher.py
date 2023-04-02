import numpy as np
import string

def create_cipher_matrix(key):
    key = key.replace(" ", "")
    key = "".join(sorted(set(key), key=key.index))

    matrix = list(key)
    alphabet = string.ascii_lowercase.replace("j", "")
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)

    matrix = np.array(matrix).reshape((5, 5))
    return matrix

def find_letter(letter, matrix):
    row, col = np.where(matrix == letter)
    return row[0], col[0]

def encode(message, key):
    matrix = create_cipher_matrix(key)

    message = message.lower().replace("j", "i")
    message = "".join(char for char in message if char.isalpha())

    if len(message) % 2 != 0:
        message += "x"

    encoded_message = ""
    for i in range(0, len(message), 2):
        letter1 = message[i]
        letter2 = message[i+1]
        row1, col1 = find_letter(letter1, matrix)
        row2, col2 = find_letter(letter2, matrix)

        if row1 == row2:
            encoded_letter1 = matrix[row1][(col1+1)%5]
            encoded_letter2 = matrix[row2][(col2+1)%5]

        elif col1 == col2:
            encoded_letter1 = matrix[(row1+1)%5][col1]
            encoded_letter2 = matrix[(row2+1)%5][col2]

        else:
            encoded_letter1 = matrix[row1][col2]
            encoded_letter2 = matrix[row2][col1]

        encoded_message += encoded_letter1 + encoded_letter2

    return encoded_message

plaintext = input("Input plaintext: ")
key = input("Enter key: ")
encoded_message = encode(plaintext, key)
print(encoded_message)