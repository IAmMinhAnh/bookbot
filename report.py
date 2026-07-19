def print_report(file_path: str, words_count: int, chars_list: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for key, value in chars_list:
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")
