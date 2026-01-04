from stats import get_num_words, get_num_chars, print_report
import sys

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_file = sys.argv[1]

words = get_num_words(book_file)
print(f"Found {words} total words") 
print(get_num_chars(book_file))
print_report(book_file)