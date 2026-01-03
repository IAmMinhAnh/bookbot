from stats import get_book_num_of_words, get_book_character_dictionary, sorting_dictionary
import sys

def report(book_link, book_num_of_words, dictionary):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_link}...")
    print("----------- Word Count ----------")
    print(f"Found {book_num_of_words} total words")
    print("--------- Character Count -------")
    for char_dict in dictionary:
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

def get_book_text(book):
    with open(book) as f:
        book_content = f.read()
    return book_content

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_link = sys.argv[1]
    book_content = get_book_text(book_link)
    book_num_of_words = get_book_num_of_words(book_content)
    book_chars_dictionary = get_book_character_dictionary(book_content)
    dictionary = sorting_dictionary(book_chars_dictionary)

    report(book_link, book_num_of_words, dictionary)
    

main()
    