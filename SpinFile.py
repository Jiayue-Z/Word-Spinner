#A4: Word Spinner, Jay Zhang, https://github.com/Jiayue-Z/Word-Spinner.git
import Spinner
import string
def main():
    with open("essay") as file:
            read = file.read()
            lower = read.lower()
            text = lower.translate(str.maketrans('', '', string.punctuation))
    print('Original:', text)
    synonym = Spinner.Spinner()
    for x in range(1,4):
        print('Option', x, ': ', synonym.replace(text))

if __name__ == '__main__':
    main()

