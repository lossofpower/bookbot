def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    returnLetters(text)

def get_book_text(path):
    with open(path) as f:
        return f.read().lower()

def returnLetters(words):
    dict = {}
    list = []
    print("working")
    for word in words:
        for letter in word:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1

    # print(dict.items())
    for k,v in dict.items():
        temp = [k,v]
        if temp[0].isalpha():
            list.append(temp)
    for item in list:
        print(f"The {item[0]} character was found {item[1]} times")


main()