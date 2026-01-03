def get_book_text(book_file="books/frankenstein.txt"):
    with open("books/frankenstein.txt", "r") as file:
        return file.read()

def get_num_words(book_file="books/frankenstein.txt"):
    words = get_book_text(book_file).split()
    return len(words)
