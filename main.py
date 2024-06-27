import argparse


def substitute(array: list, regex: str) -> list:
    _, replaced_word, new_word, _ = regex.split("/")
    new_array = []
    for text in array:
        new_array.append(text.replace(replaced_word, new_word))
    return new_array


def print_only_explicit(array: list, instruction: str) -> None:
    if instruction[-1] == "p":
        instruction = instruction.rstrip("p")
        first, last = instruction.split(",")
        for i in range(int(first)-1, int(last)):
            print(array[i])


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
    if "/" in args.regex:
        changed_quotes = substitute(array=content, regex=args.regex)
        if not args.quiet:
            for qu in changed_quotes:
                print(qu)
        else:
            _, _, new_word, _ = args.regex.split("/")
            for quo in changed_quotes:
                if new_word in quo:
                    print(quo)
    else:
        print_only_explicit(array=content, instruction=args.regex)


if __name__ == '__main__':
    main()
