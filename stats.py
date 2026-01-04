def get_book_text(book_file="books/frankenstein.txt"):
    with open(book_file, "r") as file:
        return file.read()

def get_num_words(book_file="books/frankenstein.txt"):
    words = get_book_text(book_file).split()
    return len(words)

def get_num_chars(book_file="books/frankenstein.txt"):
    text = get_book_text(book_file)
    
    dict_chars = {}
    
    for c in text:
        char = c.lower()
        if char not in dict_chars:
            dict_chars[char] = 0
        dict_chars[char] += 1

    return dict_chars

def sort_on(items):
    return items["num"]

def order_list(dict_list):
    dict_list.sort(reverse=True, key=sort_on)

def print_report(book_file="books/frankenstein.txt"):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(book_file)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = get_num_chars(book_file)
    dict_list = []
    for char, count in num_chars.items():
        if char.isalpha():
            dict_list.append({"char": char, "num": count})
    order_list(dict_list)
    for item in dict_list:
        print(f"{item['char']}: {item['num']}")
    print("============ END ===============")