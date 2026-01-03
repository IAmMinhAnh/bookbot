from stats import get_book_num_of_words, get_book_character_dictionary

def get_book_text(book):
    with open(book) as f:
        book_content = f.read()
    return book_content

def main():
    book_link = "./books/frankenstein.txt"
    book_content = get_book_text(book_link)
    book_num_of_words = get_book_num_of_words(book_content)
    book_chars_dictionary = get_book_character_dictionary(book_content)
    print(f"Found {book_num_of_words} total words")
    print(book_chars_dictionary)

main()
    