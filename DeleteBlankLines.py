import pyperclip
import sys


# -----------------------------------------------------
def delete_blank_lines(raw_file, start):
    """
    Opens the file, checks than file has more lines than start,
    go through the file deleting the blank lines and return it.
    """
    with open(raw_file, 'r', encoding='utf-8') as file:
        file_length = len(file.readlines())
        clean_file = ''
        c = 0

        if (file_length < start):
            raise Exception()

        for line in file:
            c += 1
            if c >= start:
                if line not in ['\n', '\r\n']:
                    clean_file = clean_file+line
        file.close()
        return clean_file


# -----------------------------------------------------
def clipboard(to_clipboard):
    """Simply copy the string apssed to clipboard"""
    pyperclip.copy(to_clipboard)


# -----------------------------------------------------
def main():
    """Gets the arguments passed, cleans the file and copy it to the clipboard."""
    try:
        raw_file = sys.argv[1]
    except:
        print('You need to pass a file for the first argument.')
    else:
        try:
            start = int(sys.argv[2])
        except:
            start = 0
        finally:
            try:
                clean_file = delete_blank_lines(raw_file, start)
            except:
                print('The file is shorter than start.')
            else:
                clipboard(clean_file)
                print('Succesfully copied to clipboard.')


if (__name__ == "__main__"):
    main()
