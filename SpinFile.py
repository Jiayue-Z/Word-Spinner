#A4: Word Spinner, Jay Zhang, https://github.com/Jiayue-Z/Word-Spinner.git
import Spinner
import string
def main():
    with open("Essay.txt") as file:
            read = file.read()
            lower = read.lower()
            text = lower.translate(str.maketrans('', '', string.punctuation))
    synonym = Spinner.Spinner()
    synonym.replace(text)

if __name__ == '__main__':
    main()

