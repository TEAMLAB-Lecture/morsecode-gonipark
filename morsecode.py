# -*- coding: utf8 -*-

import test_morsecode as tm
# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    if user_input.lower() in ['h','help']:
        return True
    return False

def is_validated_english_sentence(user_input):
    accepted_marks='.,!?- '
    new_input=''
    
    for i in user_input:
        if not i.isalpha():
            if i not in accepted_marks:
                return False
        else:
            new_input+=i
        if i=='-':
            new_input+=i

    if len(new_input)==0:
        return False
    elif set(new_input)=={'-'}:
        return False
    else:
        return True


def is_validated_morse_code(user_input):
    for i in user_input:
        if i not in ['.','-',' ']:
            return False
    splited_user_input=user_input.split()
    morse_code_dict=get_morse_code_dict()
    for i in splited_user_input:
        if i not in morse_code_dict.values():
            return False
    return True


def get_cleaned_english_sentence(raw_english_sentence):
    sentence_marks='.,!?'

    raw_english_sentence = raw_english_sentence.strip()
    for i in sentence_marks:
        raw_english_sentence = raw_english_sentence.replace(i,'')

    return raw_english_sentence

def decoding_character(morse_character):
    morse_code_dict = get_morse_code_dict()
    for key,value in morse_code_dict.items():
        if value==morse_character:
            return key

def encoding_character(english_character):
    morse_code_dict = get_morse_code_dict()
    return morse_code_dict[english_character.upper()]

def decoding_sentence(morse_sentence):
    morse_list=morse_sentence.split(' ')
    result=''
    for morse_mark in morse_list:
        if morse_mark != '':
            character=decoding_character(morse_mark)
            result+=character
        else:
            result+=' '
    return result


def encoding_sentence(english_sentence):
    cleaned_sentence=get_cleaned_english_sentence(english_sentence)
    sentences=cleaned_sentence.split()

    morse_sentence=''

    for word in sentences:
        for character in word:
            morse_sentence += encoding_character(character)
            morse_sentence+=' '
        morse_sentence+=' '

    return morse_sentence.strip()

def main():
    print("Morse Code Program!!")

    while(True):
        user_input=input("Input your message(H - Help, 0 - Exit: ")

        if(not(is_validated_english_sentence(user_input) or is_validated_morse_code(user_input))):
            if user_input=="0":
                break
            print("Wrong Input")
            # user_input=input("Input your message(H - Help, 0 - Exit: ")

        elif is_help_command(user_input):
            print(get_help_message())
        elif is_validated_morse_code(user_input):
            print(decoding_sentence(user_input))
        elif is_validated_english_sentence(user_input):
            print(encoding_sentence(user_input))
            
    
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":

    
    
  

    main()
