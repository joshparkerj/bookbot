def main():
    file_name = "./books/frankenstein.txt"
    print(get_report_heading(file_name))
    file_contents = get_file_contents(file_name)
    print(get_word_count_report(file_contents))
    print("")
    print(get_char_counts_report(file_contents))
    print("--- End report ---")


def get_report_heading(file_name):
    return f"--- Begin report of {file_name[2:]} ---"


def get_word_count_report(file_contents):
    char_count = len(file_contents)
    word_count = len(file_contents.split())
    line_count = len(file_contents.split("\n")) - 1
    return (
        f"{line_count} lines, {word_count} words, and {char_count} "
        + "characters found in the document"
    )


def get_file_contents(file_name):
    with open(file_name) as f:
        return f.read()


def get_char_counts(text):
    char_count_dict = {char: 0 for char in set(text.lower())}
    for char in text.lower():
        char_count_dict[char] += 1
    return char_count_dict


def show_new_line_escape_character(count_dict):
    return "\\n" if count_dict["char"] == "\n" else count_dict["char"]


def show_plural(count_dict):
    return "" if count_dict["count"] == 1 else "s"


def get_char_counts_report(text):
    char_counts = get_char_counts(text)
    list_of_dicts = [
        {"char": char, "count": count} for char, count in char_counts.items()
    ]
    # filter to only alpha chars
    list_of_dicts = [d for d in list_of_dicts if d["char"].isalpha()]

    list_of_dicts.sort(reverse=True, key=lambda d: d["count"])
    return "\n".join(
        [
            (
                f"The '{show_new_line_escape_character(count_dict)}' "
                + "character "
                + f"was found {count_dict['count']} "
                + f"time{show_plural(count_dict)}"
            )
            for count_dict in list_of_dicts
        ]
    )


main()
