import argparse


def headtail(option: str, filename: str, start: int, end: int, h):
    file = open(filename)
    lines = []
    line = file.readlines()

    if option == "head":
        lines.append(line[:start])
    elif option == "tail":
        lines.append(line[-end:])
    elif option == "headtail":
        lines.append(line[:start])
        lines.append(line[-end:])
    else:
        SyntaxError("Not an option, try again")
        
    
    print(lines)


def main():
    parser = argparse.ArgumentParser(description='Create Head-Tail program.')
    subparsers = parser.add_subparsers(
            dest="subparser_name", help="sub-command help"
        )

    parser_head = subparsers.add_parser("headtail", help="Show first x lines of document.")
    parser_head.add_argument('--o', '-option', type=str, help='choose which you want, head, tail, headtail')
    parser_head.add_argument('--f', '-file', type=str, help='Choose file')
    parser_head.add_argument('--s', '-start', type=int, default=3, help='Choose how many lines to show from the start (default: 3)')
    parser_head.add_argument('--e', '-end', type=int, default=3, help='Choose how many lines to show from the end (default: 3)')
    
    args = parser.parse_args()

    headtail(args.option, args.file, args.start, args.start)


if __name__ == '__main__':
    main()