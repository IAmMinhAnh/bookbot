from stats import get_num_words, count_chars, chars_dict_to_sorted_list
from report import print_report

import sys

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main() -> None:
    args = sys.argv 
    
    if len(args) > 1:
        contents = get_book_text(args[1])
        num_words = get_num_words(contents)
        char_dict = count_chars(contents)
        char_list = chars_dict_to_sorted_list(char_dict)
        print_report(args[1], num_words, char_list)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

if __name__ == "__main__":
    main()
