#A4: Word Spinner, Jay Zhang, https://github.com/Jiayue-Z/Word-Spinner.git
import Spinner
def main():
    with open("test-synonyms.txt") as file:
            text = file.read()
    synonym = Spinner.Spinner()
    synonym.replace()

if __name__ == '__main__':
    main()

