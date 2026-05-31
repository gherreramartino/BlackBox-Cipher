OPTIONS = 4
txt = []
txt_result = []
def main():
    clear_terminal()
    print("-----Welcome to BlackBox Cipher!-----")
    option = get_valid_answer()
    
    if option == 1:        
        caesar_encrypt()
    elif option == 2:
        caesar_decrypt()
    elif option == 3:
        vigeneres_encrypt()
    elif option == 4:
        vigeneres_decrypt()
        
    
def clear_terminal():
    """This functions cleans the terminal"""
    for i in range(100):
        print('\n')

def get_valid_answer():
    """This function makes sure the user is choosing a valid answer"""
    valid_answer = False
    while valid_answer == False:
        answer = input((
        "1: Encrypt using Caesar's Cipher\n" \
        "2: Decrypt a Caesar's Cipher message\n" \
        "3: Encrypt using Vigenère's Cipher\n" \
        "4: Decrypt a Vigenère's Cipher message\n"
        "\nPlease select an option: "))
        if not(answer.isdigit()):
                clear_terminal()
                print(f"You must enter a number from 1 to {OPTIONS}")
        else:
            answer = int(answer)
            if  answer < 1 or answer > OPTIONS:
                clear_terminal()
                print(f"You must enter a number from 1 to {OPTIONS}")
            else:
                valid_answer = True
    
    return answer

def caesar_encrypt():
    """Asks the user for a message and a key and prints on 
    the terminal the message ciphered using caesar's method"""
    print("-----Caesar's Cyper Encryption-----")
    user_text = input("Paste here your text: ").upper()
    user_text = user_text.replace(' ','')
    key_input = input("Enter your key: ")
    b = key_Check_Caesar(key_input)

    for ch in user_text:
        if 'A' <= ch <= 'Z':
            txt.append(chr((ord(ch) - 65 + b) % 26 + 65))
        else:
            txt.append(ch)
    format_txt_result()
    txt_results_toString()

def format_txt_result():
    for i in range (0,len(txt),5):
        group = ''.join(txt[i:i+5])
        txt_result.append(group)

def txt_results_toString():
    final = ''
    for i in range (len(txt_result)):
        final = final + txt_result[i] + ' '
    print(final)

def caesar_decrypt():
    """Takes a text encrypted using caesar's method and it's key 
    and prints the decrypted message"""
    print("-----Caesar's Cyper Decryption-----")
    user_text = input("Paste here your text: ").upper()
    user_text = user_text.replace(' ','')
    key_input = input("Enter your key: ")
    b = key_Check_Caesar(key_input)

    for ch in user_text:
        if 'A' <= ch <= 'Z':
            txt.append(chr((ord(ch) - 65 +26 -b) % 26 + 65))
        else:
            txt.append(ch)
    format_txt_result()
    txt_results_toString()

def key_Check_Caesar(key_input):
    """This function checks the key is valid and converts it to a number so it
    can be used for encrypting the message.
    """
    if key_input.isdigit():
        b = int(key_input)

    else:
        key_input = key_input.strip().upper()
        if len(key_input) != 1 or not key_input.isalpha():
            print("Invalid key. Enter a number or a single letter.")
            return
        b = ord(key_input) - 65
    return b

def vigeneres_encrypt():
    """Asks the user for a message and a key and prints on 
    the terminal the message ciphered using vigenere's method"""
    print("-----Vigenère's Cyper Encryption-----")
    user_text = input("Paste here your text: ").upper()
    user_text = user_text.replace(' ','')
    key_input = input("Enter your key: ")
    key_b = key_Check_Vigeneres(key_input)

    for i in range(len(user_text)):
        if 'A' <= user_text[i] <= 'Z':
            txt.append(chr((ord(user_text[i]) - 65 +key_b[i%4]) % 26 + 65))
        else:
            txt.append(user_text[i])
    format_txt_result()
    txt_results_toString()
    

def key_Check_Vigeneres(key_input):
    """This function checks the key is valid and converts it to a list of numbers so it
    can be used for encrypting the message.
    """
    key_b = []
    key_input = key_input.strip().upper()
    if not key_input.isalpha():
        print("Invalid key.")
        return
    else:
        for i in range(len(key_input)):
            key_b.append(ord(key_input[i]) - 65)
    
    return key_b

def vigeneres_decrypt():
    """Takes a text encrypted using vigeneres method and it's key and "
    prints the decrypted message"""
    print("-----Vigenère's Cyper Decryption-----")
    user_text = input("Paste here your text: ").upper()
    user_text = user_text.replace(' ','')
    key_input = input("Enter your key: ")
    key_b = key_Check_Vigeneres(key_input)

    for i in range(len(user_text)):
        if 'A' <= user_text[i] <= 'Z':
            txt.append(chr((ord(user_text[i]) - 65 +26 -key_b[i%4]) % 26 + 65))
        else:
            txt.append(user_text[i])
    format_txt_result()
    txt_results_toString()
    

if __name__ == "__main__":
    main()