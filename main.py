"""Analyse the text of Frankenstein."""


def sort_on(char_dict):
    """Return the count of a dictionary."""
    return char_dict["count"]


def read_file(file_path):
    """Read the contents of a file."""
    with open(file_path, encoding="utf-8") as f:
        return f.read()


def count_words(text):
    """Count the number of words in text."""
    word_list = text.split()
    return len(word_list)


def count_characters(text):
    """Count the number of characters in text."""
    characters = {}
    char_count_dicts = []
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

    for char, count in characters.items():
        char_count_dicts.append({"char": char, "count": count})

    char_count_dicts.sort(key=sort_on, reverse=True)

    return char_count_dicts


def create_report(word_count, character_count_dicts):
    """Create a report of the word and character counts."""
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"The text contains {word_count} words.\n"
    report += "The character counts are as follows:\n"
    for char_dict in character_count_dicts:
        report += f"{char_dict['char']}: {char_dict['count']}\n"
    report += "--- End report ---"
    return report


def main():
    """Run the main program."""
    text = read_file("books/frankenstein.txt")
    word_count = count_words(text)
    character_count_dicts = count_characters(text)
    report = create_report(word_count, character_count_dicts)
    print(report)


main()
