
def main() -> int:
    report = get_report("books/frankenstein.txt")
    print (report)
    return 0

def get_report(book_path: str) -> str:
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_dict = get_letter_dict(text)
    sorted_character_counts = get_dict_as_list(character_dict, True)
    report = f"--- Report of {book_path} ---"
    report += f"\n{word_count} words found in the document"
    for char_dict in sorted_character_counts:
        report += f"\nThe '{char_dict['character']}' character was found {char_dict['count']} times."
    report += "\n--- End Report ---"
    return report

def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_letter_dict(text: str) -> dict[str, int]:
    letter_counts = {}
    lowered_text = text.lower()
    for c in lowered_text:
        if c.isalpha():
            if c in letter_counts.keys():
                letter_counts[c] = letter_counts[c] + 1
            else:
                letter_counts[c] = 1
    return letter_counts

def sort_by_count(dict):
    return dict["count"]

def get_dict_as_list(character_dict : dict[str,int], sorted:bool = True):
    dict_list = []
    for key in character_dict.keys():
        dict_list.append({"character":key, "count":character_dict[key]})
    if sorted:
        dict_list.sort(reverse=True, key=sort_by_count)
    return dict_list

main()