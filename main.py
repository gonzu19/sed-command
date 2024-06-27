import sys

def main() -> None:
    regex = sys.argv[1]
    file = sys.argv[2]
    with open(file, "r") as read_file:
        content = read_file.readlines()
    changed_quotes = []
    _,replaced_word,new_word,_ = regex.split("/")
    for quote in content:
        changed_quotes.append(quote.replace(replaced_word,new_word))
    for qu in changed_quotes:
        print(qu)


if __name__ == '__main__':
    main()
