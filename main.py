from stats import get_num_words # type: ignore
from stats import  get_character_number
import sys

try:
    
    path_to_file = sys.argv[1]
    char_dictonary = {}
    word_count = 0
    full_text = ""
    with open(path_to_file) as f:
        full_text = f.read()

    word_count = get_num_words(full_text)
    char_dictonary = get_character_number(full_text)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_dictonary:
        print(f"{char}: {char_dictonary[char]}")

except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


