import argparse


def substitute(array: list, regex: str) -> list:
    _, replaced_word, new_word, _ = regex.split("/")
    new_array = []
    for text in array:
        if text != "\n":
            new_array.append(text.replace(replaced_word, new_word))
    return new_array


def print_only_explicit(array: list, instruction: str) -> str:
    cad = ""
    if instruction[-1] == "p":
        instruction = instruction.rstrip("p")
        first, last = instruction.split(",")
        for i in range(int(first)-1, int(last)):
            cad += array[i]
            print(array[i].rstrip())
    return cad


def filtering(array: list, word: str) -> str:
    cad = ""
    for quote in array:
        if word in quote:
            cad += word
            print(quote.rstrip())
    return cad


def print_with_double_line_jump(array: list) -> str:
    cad = ""
    for element in array:
        if element != "\n":
            print(element)
            cad += element
    return cad


def overwrite_file(info: str, filename: str) -> None:
    with open(filename,"w") as file:
        file.write(info)


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
    parser.add_argument('-i',
                        '--overwrite',
                        action='store_true',
                        help='overwrittes the original file '
                        )
    args = parser.parse_args()
    with open(args.filename, "r") as read_file:
        content = read_file.readlines()
    parts_of_regex = args.regex.split("/")
    output = ""
    if parts_of_regex[0] == "s" and len(parts_of_regex) == 4:
        changed_quotes = substitute(array=content, regex=args.regex)
        if not args.quiet:
            for qu in changed_quotes:
                output += qu
                print(qu.rstrip())
        else:
            _, _, new_word, _ = parts_of_regex
            for quo in changed_quotes:
                if new_word in quo:
                    output += quo
                    print(quo.rstrip())

    elif len(parts_of_regex) == 1 and parts_of_regex[0] == "G":
        output = print_with_double_line_jump(array=content)
    elif len(parts_of_regex) == 3:
        output = filtering(array=content, word=parts_of_regex[1])

    elif len(parts_of_regex) == 1:
        output = print_only_explicit(array=content, instruction=args.regex)
    if args.overwrite:
        overwrite_file(info=output, filename=args.filename)


if __name__ == '__main__':
    main()
