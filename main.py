def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(word_counter(text))
    letter_counter(text)
def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    return len(text.split())
    
def letter_counter(text):
    letters = {}
    for letter in text:
        char = letter.lower()
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    print(letters)
    pass
main()