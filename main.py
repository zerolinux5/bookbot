import sys

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
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    content = get_book_text(file_path)
    word_count = count_words(content)
    char_count = char_usage(content)
    sorted_item_list = usage_to_sorted_list(char_count)
    print_report(file_path, word_count, sorted_item_list)


main()
