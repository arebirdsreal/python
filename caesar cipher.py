alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def caesar(text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet) #using modulo operator, shifted position is kept within 0 and 26, otherwise indices like 27,28,etc will give error as there is nothing at those indices
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d string: {output_text}")

caesar(text, shift, direction)







#for decoding:
"""def decrypt(cipher_text, shift_amount):
    original_text = ""
    for letter in cipher_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position = shifted_position % len(alphabet)
        original_text += alphabet[shifted_position]
    print(f"Here is the decoded string: {original_text}")

    #for encoding: same but using shifted_position = alphabet.index(letter) + shift_amount

caesar(text,shift)"""


