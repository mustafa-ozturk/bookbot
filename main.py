def main():
    book_path = "books/frankenstein.txt";
    text = get_book_text(book_path)
    wc = get_word_count(text)
    print(wc)

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_word_count(text):
    return len(text.split());

main()
