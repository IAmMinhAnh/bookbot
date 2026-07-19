def get_num_words(contents: str) -> int:
    split_contents = contents.split()
    return len(split_contents)

def count_chars(contents: str) -> dict[str, int]:
    chars = {}
    for c in contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(char_tuple: tuple[str, int]) -> int:
    return char_tuple[1]

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    chars_list = []
    for key in chars_dict:
        chars_list.append((key, chars_dict[key]))
    sorted_chars_list = sorted(chars_list, reverse=True, key=sort_on)
    return sorted_chars_list

