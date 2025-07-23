import sys
from stats import count_words
from stats import count_char
from stats import sort_dictionary

#def get_book_text(file_path):
#   with open(file_path) as f:
#        return f.read()
#
#def count_words(file_path):
#    contents = get_book_text(file_path)
#    words = contents.split()
#    return len(words)
#
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    wordcount = count_words(file_path)
    print(f"Found {wordcount} total words")
    #char_count = count_char(file_path)
    #print(char_count)
    dict_sort = sort_dictionary(file_path)
    for char, count in dict_sort:
        if char.isalpha():
            print(f"'{char}: {count}'")

main()
