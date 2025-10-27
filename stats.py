def count_words(content):
    return len(content.split())


def char_usage(content):
    usage_mapping = {}
    for char in content:
        char = char.lower()
        if char not in usage_mapping:
            usage_mapping[char] = 1
        else:
            usage_mapping[char] += 1
    return usage_mapping
