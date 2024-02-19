#A4: Word Spinner, Jay Zhang, https://github.com/Jiayue-Z/Word-Spinner.git
import random
class Spinner:
    def __init__(self):
        self.diction = {}
        with open("test-synonyms.txt") as file:
            for line in file:
                word = line.split(':')
                word[1] = word[1].strip()
                word[1] = word[1].split(',')
                self.diction[word[0]] = word[1]
            print(self.diction)
            print(len(self.diction['person']))
    def replace(self,text):
        essay = text.split()
        new_text = ''
        for x in essay:
            if x in self.diction:
                print(self.diction[x])
                if random.randrange(1,100) > 50:
                    if len(self.diction[x]) > 1:
                        new_text += self.diction[x][random.randrange(0, len(self.diction))] + ' '
                    else:
                        new_text +=  self.diction[x][0] + ' '
                else:
                    new_text += x + ' '
            else:
                new_text += x + ' '
        return new_text




yes = 'He is a good person and a bad person.'
test = Spinner()
print(test.replace(yes))