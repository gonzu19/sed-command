import argparse


def substitute(array: list, regex: str) -> list:
    _, replaced_word, new_word, _ = regex.split("/")
    new_array = []
    for text in array:
        new_array.append(text.replace(replaced_word, new_word))
    return new_array


def main() -> None:
    parser = argparse.ArgumentParser(
                                    description="Count lines, words, "
                                                "or characters in a file.")
    parser.add_argument('regex',
                        type=str,
                        help='regex used to substitute',
                        nargs="?"
                        )
    parser.add_argument('filename',
                        type=str,
                        help='The file to process.',
                        nargs="?"
                        )
    parser.add_argument('-n',
                        '--quiet',
                        action='store_true',
                        help='Does not output the result of the command '
                        'unless there is explicit instruction to'
                        )

    args = parser.parse_args()
    with open(args.filename, "r") as read_file:
        content = read_file.readlines()
    changed_quotes = substitute(array=content, regex=args.regex)
    for qu in changed_quotes:
        print(qu)


if __name__ == '__main__':
    main()
