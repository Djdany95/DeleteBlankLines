import pyperclip, webbrowser, sys

def get_lines(file, line):
    with open(file,'r', encoding='utf-8') as file:
        cleanFile=''
        c=0
        for line in file:
            c+=1
            if c>=line:
                if line not in ['\n', '\r\n']:
                    cleanFile=cleanFile+line
        file.close()
        return cleanFile

def clipboard(to_clipboard):
    pyperclip.copy(to_clipboard)

def main():
    file=sys.argv[1]
    line=0
    if sys.argv[2]:
        line=sys.argv[2]
    newFile=get_lines(file, line)
    clipboard(newFile)

main()