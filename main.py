def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print()
    print(f"{num_words} words found in the document")
    print()
    for item in chars_sorted_list:
        print(f"The {item[0]} character was found {item[1]} times")
    print()
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read().lower()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    print("working")
    for word in text:
        for letter in word:
            if letter in chars:
                chars[letter] += 1
            else:
                chars[letter] = 1
    return chars

def chars_dict_to_sorted_list(chars_dict):
    list = []
    for k,v in chars_dict.items():
        temp = [k,v]
        if temp[0].isalpha():
            list.append(temp)
    list.sort()
    return list


main()