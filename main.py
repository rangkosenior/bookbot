def get_text_from_file(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def unique_characters(text, only_alpha = False):
    characters = {}
    for char in text:
        if not char.isalpha() and only_alpha:
            continue
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def print_report(book_path):
    contents = get_text_from_file(book_path)
    word_count = count_words(contents)
    unique_chars = unique_characters(contents, True)
    list_chars = [{"char": char, "num": count} for char, count in unique_chars.items()]
    def sort_on(dict):
        return dict["num"]
    list_chars.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for dict in list_chars:
        char = dict["char"]
        count = dict["num"]
        print(f"The {char} character was found {count} times")
    print("--- End Report ---")

def main():
    frankenstein_path = "books/frankenstein.txt"
    
    print_report(frankenstein_path)

main()