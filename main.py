def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    get_report(text, book_path)


def get_report(text, book_path):
    chars_dict = get_chars_dict(text)

    chars_list = convert_dict_to_list_sorted(chars_dict)

    print(f"----- Begin Report of {book_path} -----")

    for item in chars_list:
        if item["char"].isalpha():
            print(f"The '{item["char"]}' character was found {item["num"]} times")

    print(f"----- End Report -----")

def sort_on(d):
    return d["num"]

def convert_dict_to_list_sorted(dict):
    item_list = []
    for key in dict:
        item_list.append({"char": key, "num": dict[key]})

    item_list.sort(reverse=True, key=sort_on)

    return item_list

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_chars_dict(text):
    letters_dict = {}
    for i in text.lower():
        if i not in letters_dict:
            letters_dict[i] = 0

        letters_dict[i] += 1

    return letters_dict

main()
