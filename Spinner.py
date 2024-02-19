#A4: Word Spinner, Jay Zhang, https://github.com/Jiayue-Z/Word-Spinner.git
import random
class Spinner:
    def __init__(self):
        self.diction = {}
        with open("synonyms-simplified.txt") as file:
            for line in file:
                word = line.split(':')
                word[1] = word[1].strip()
                word[1] = word[1].split(',')
                self.diction[word[0]] = word[1]
    def replace(self,text):
        essay = text.split()
        new_text = ''
        for x in essay:
            if x in self.diction:
                if random.randint(1,100) > 50:
                    new_text += self.diction[x][random.randrange(0, len(self.diction[x]))] + ' '
                else:
                    new_text += x + ' '
            else:
                new_text += x + ' '
        return new_text