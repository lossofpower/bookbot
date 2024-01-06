with open("books/frankenstein.txt") as f:
    file_contents = f.read().lower()
    words = file_contents.split()

def returnLetters():
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


returnLetters()