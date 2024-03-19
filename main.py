def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_counter(text)
    chars = letter_counter(text)
    unsorted_dict = dictionarinator(chars)
    unsorted_dict.sort(reverse=True, key=sort_on)
    formater(book_path, words, unsorted_dict)

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
    return letters

#converts dictionary into a list of dictionaries
def dictionarinator(dict):
    dict_list = []
    for char in dict:
        if char.isalpha() is True:
            dict_list.append({"char": char, "num":  dict[char]})
        else:
            pass
    return dict_list

def sort_on(dict):
    return dict["num"]

def formater(document, wc, dict):
    print(f"--- Begin report of {document} ---")
    print(f"{wc} words found in the docuemnt \n")
    for item in dict:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End report ---")
    

main()
