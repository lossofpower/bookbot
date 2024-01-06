with open("books/frankenstein.txt") as f:
    file_contents = f.read().lower()
    words = file_contents.split()

def returnLetters():
    dict = {}
    print("working")
    for word in words:
        for letter in word:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1

    print(dict)

returnLetters()