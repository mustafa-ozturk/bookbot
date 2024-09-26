def main():
    book_path = "books/frankenstein.txt";
    text = get_book_text(book_path)
    wc = get_word_count(text)
    chars_dict = get_char_count_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print_report(book_path, wc, chars_sorted_list)

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

def chars_dict_to_sorted_list(dict):
    sorted_list = [];
    for key in dict:
        sorted_list.append({"char": key, "count": dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list;

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
