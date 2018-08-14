import pyperclip
import sys


def get_lines(raw_file, start):
    with open(raw_file, 'r', encoding='utf-8') as file:
        clean_file = ''
        c = 0
        for line in file:
            c += 1
            if c >= start:
                if line not in ['\n', '\r\n']:
                    clean_file = clean_file+line
        file.close()
        return clean_file


def clipboard(to_clipboard):
    pyperclip.copy(to_clipboard)


def main():
    try:
        raw_file = sys.argv[1]
    except:
        print('File is necessary')

    if len(sys.argv) == 3:
        start = sys.argv[2]
    else:
        start = 0

    clean_file = get_lines(raw_file, start)
    clipboard(clean_file)


main()
