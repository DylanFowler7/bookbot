def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) 
    number = 0
    words = text.split()
    chars_dict = characters(text)
    sorted_characters = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
    print('--- Begin report of books/frankenstein.txt ---')
    for i in words:
        number += 1
    print(number, 'words found in the document')
    for other, count in sorted_characters:
        print(f"The '{other}' character was found {count} times")
    print("---End report---")
    
    
    
def characters(text):
    other = {}
    for l in text:
        lower = l.lower()
        if lower.isalpha():
            if lower in other:
                other[lower] += 1
            else: 
                other[lower] = 1
    return other

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def sort(chars_dict):
    return chars_dict["num"]


main()
