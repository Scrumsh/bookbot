def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(word_counter(text))
def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    return len(text.split())
    
main()