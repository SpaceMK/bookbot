def get_num_words(full_text):
    number_of_words = len(full_text.split())
    return number_of_words

def get_character_number(full_text):
    char_dict = {}
    for letter in full_text.lower():
        if(letter not in char_dict):
            char_dict[letter] = 1
        else:
            char_dict[letter] += 1
    return char_dict
            