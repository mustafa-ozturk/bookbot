def main():
    book_path = "books/frankenstein.txt";
    text = get_book_text(book_path)
    wc = get_word_count(text)
    char_count_dict = get_char_count_dict(text)
    char_count_dict_list = get_char_count_dict_list(char_count_dict)
    char_count_dict_list.sort(reverse=True, key=sort_on)
    print_report(book_path, wc, char_count_dict_list)

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_word_count(text):
    return len(text.split());

def get_char_count_dict(text):
    chars = {}
    for c in text:
        lc = c.lower()
        if lc not in chars:
            chars[lc] = 0
        chars[lc] += 1
    return chars

def get_char_count_dict_list(dict):
    char_count_dict_list = [];
    for key in dict:
        char_count_dict_list.append({"char": key, "count": dict[key]})
    return char_count_dict_list;

def sort_on(dict):
    return dict["count"]

def print_report(book_path, wc, list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{wc} words found in the document\n")

    for cc in list:
        if cc["char"].isalpha():
            print(f"The '{cc["char"]} character was found '{cc["count"]}' times")
    print(f"--- End Report ---")


main()
