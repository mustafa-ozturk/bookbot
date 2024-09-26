def main():
    book_path = "books/frankenstein.txt";
    text = get_book_text(book_path)
    wc = get_word_count(text)
    char_count_dict = get_character_dict(text)
    print(char_count_dict)

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_word_count(text):
    return len(text.split());

def get_character_dict(text):
    chars = {}
    for c in text:
        lc = c.lower()
        if lc not in chars:
            chars[lc] = 0
        chars[lc] += 1
    return chars

main()
