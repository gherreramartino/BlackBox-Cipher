OPTIONS = 4
txt = []
txt_result = []
def main():
    clear_terminal()
    print("-----Welcome to BlackBox Cipher!-----")
    option = get_valid_answer()
    
    if option == 1:        
        Caesar_encrypt()
    elif option == 2:
        print("-----Caesar's Cyper Decryption-----")
    elif option == 3:
        print("-----Vigenère's Cyper Encryption-----")
    elif option == 4:
        print("-----Vigenère's Cyper Decryption-----")
        
    
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

def Caesar_encrypt():
    print("-----Caesar's Cyper Encryption-----")
    user_text = input("Paste here your text: ").upper()
    user_text = user_text.replace(' ','')
    key_input = input("Enter your key: ")

    if key_input.isdigit():
        b = int(key_input)

    else:
        key_input = key_input.strip().upper()
        if len(key_input) != 1 or not key_input.isalpha():
            print("Invalid key. Enter a number or a single letter.")
            return
        b = ord(key_input) - 65

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
if __name__ == "__main__":
    main()