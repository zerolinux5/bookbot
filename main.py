from stats import count_words, char_usage, usage_to_sorted_list


def get_book_text(file_path):
    contents = ""
    with open(file_path) as fd:
        contents = fd.read()
    return contents


def print_report(file_path, word_count, sorted_item_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_item_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")


def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_content = get_book_text(frankenstein_path)
    word_count = count_words(frankenstein_content)
    char_count = char_usage(frankenstein_content)
    sorted_item_list = usage_to_sorted_list(char_count)
    print_report(frankenstein_path, word_count, sorted_item_list)


main()
