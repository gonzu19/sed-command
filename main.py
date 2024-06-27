import sys


def substitute(array: list, regex: str) -> list:
    _, replaced_word, new_word, _ = regex.split("/")
    new_array = []
    for text in array:
        new_array.append(text.replace(replaced_word, new_word))
    return new_array


def main() -> None:
    regex, file = sys.argv[1], sys.argv[2]
    with open(file, "r") as read_file:
        content = read_file.readlines()
    changed_quotes = substitute(array=content, regex=regex)
    for qu in changed_quotes:
        print(qu)


if __name__ == '__main__':
    main()
