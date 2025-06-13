from contextlib import nullcontext
from Sentence import Sentence
from Word import Word

class Reader:

    def __init__(self):
        self.sentences = []

    def read_text(self, text):
        lines = text.splitlines()
        sentence = None
        sentence_value = ""
        sen_index = 1
        word_start = 0

        for index, line in enumerate(lines):
            if line.startswith("#Text") and len(line) > 6:
                value = line[6:]
                sentence_value = sentence_value + value
                if not lines[index + 1].startswith("#Text"):
                    sentence = Sentence(sen_index, sentence_value)
                    self.sentences.append(sentence)
                    word_start = 0
                    sen_index = sen_index + 1
                    
            elif line.startswith("#"):
                word_start = 0
            elif line!= "":
                sentence_value = ""
                tsv = line.split('\t')
                word_index = int(tsv[0].split('-')[1])
                word_value = tsv[2]
                word_end = word_start + len(word_value)
                word = Word(word_index, word_start, word_end, word_value)
                label_str = tsv[3].split('|')
                sentence.add_word(word)
                for label in label_str:
                    sentence.add_word_label(word, label)

        return self.sentences