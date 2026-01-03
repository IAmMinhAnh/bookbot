def sorting_dictionary(dictionary):
    def sort_on(items):
        return items["num"]

    list_of_chars = []
    for char in dictionary:
        temp_dict = {}
        temp_dict["char"] = char
        temp_dict["num"] = dictionary[char]
        list_of_chars.append(temp_dict)

    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars


def get_book_character_dictionary(content):
    content = content.lower()
    dictionary = {}
    for char in content:
        if (char not in dictionary and char != " " and char.isalpha()):
            count = 0
            for sub_char in content:
                if (sub_char == char):
                    count += 1
            dictionary[char] = count
    return dictionary

def get_book_num_of_words(content):
    book_num_of_words = content.split()
    return len(book_num_of_words)