def get_book_text(file_path):
   with open(file_path) as f:
        return f.read()

def count_words(file_path):
    contents = get_book_text(file_path)
    words = contents.split()
    return len(words)

def count_char(file_path):
    contents = get_book_text(file_path)
    char_counts = {}
    for char in contents.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_dictionary(file_path):
    dictionary = count_char(file_path)
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    return sorted_items
