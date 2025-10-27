from stats import count_words, char_usage


def get_book_text(file_path):
    contents = ""
    with open(file_path) as fd:
        contents = fd.read()
    return contents


def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_content = get_book_text(frankenstein_path)
    word_count = count_words(frankenstein_content)
    print(f"Found {word_count} total words")
    char_count = char_usage(frankenstein_content)
    print(char_count)


main()
