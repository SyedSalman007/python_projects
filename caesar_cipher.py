alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def ceaser_function(position, user_data, shift_num):
    if position == "encrypt":

        encrypted_string = ""
        for val in user_data:
            if val == ' ' or val in number:
                encrypted_string += val
            else:
                index_num = alphabet.index(val)
                try:
                    encrypted_letter = alphabet[index_num + shift_num]
                except IndexError:
                    encrypted_letter = alphabet[(index_num + shift_num) - 26]
                encrypted_string += encrypted_letter
        print(encrypted_string)

    elif position == "decrypt":
        decrypted_string = ""
        for val in user_data:
            if val == ' ' or val in number:
                decrypted_string += val
            else:
                index_num = alphabet.index(val)
                try:
                    decrypted_letter = alphabet[index_num - shift_num]
                except IndexError:
                    decrypted_letter = alphabet[(index_num - shift_num) + 26]
                decrypted_string += decrypted_letter
        print(decrypted_string)
    else:
        print("\nInvalid data entered")
        return None


val = ''

while val != 'no':
    flow = input("Enter encrypt or decrypt: ").lower()
    if flow == "decrypt":
        text = input("Enter the text to be decoded : ").lower()
    else:
        text = input("Enter the text to be encoded : ").lower()
    shift_value = int(input("Enter the shift value : "))

    ceaser_function(position=flow, user_data=text, shift_num=shift_value)

    val = input("To continue type 'yes', to exit type 'no': ").lower()
