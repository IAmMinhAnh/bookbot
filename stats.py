def get_book_character_dictionary(content):
    content = content.lower()
    dictionary = {}
    for char in content:
        if (char not in dictionary and char != " "):
            count = 0
            for sub_char in content:
                if (sub_char == char):
                    count += 1
            dictionary[char] = count
    return dictionary

def get_book_num_of_words(content):
    book_num_of_words = content.split()
    return len(book_num_of_words)