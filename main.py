def word_count(data):
    return len(data.split())

def letter_count(data):
    temp = data.lower()
    dict = {}
    for char in temp:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_on(dict):
    return dict["count"]

def report(book, filename):
    wordcount = word_count(book)
    lettercount = letter_count(book)
    temp = []
    for letter in lettercount:
        if letter.isalpha():
            entry = {}
            entry["char"] = letter
            entry["count"] = lettercount[letter]
            temp.append(entry)
    temp.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {filename} ---")
    print(f"Document contained {wordcount} words.\n")
    for row in temp:
        print(f"The character '{row["char"]}' appeared {row["count"]} times.")
    print("--- End report ---")

def main():
    fname = "books/frankenstein.txt"
    with open(fname) as f:
        file_contents = f.read()
    report(file_contents, fname)

main()