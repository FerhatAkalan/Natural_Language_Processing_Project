import os

from Reader import Reader
from Sentence import Sentence
from Word import Word

class ChunkingLoader:

    def __init__(self, filename):
        self.folder = filename
        self.reader = Reader()
        self.sentences = [];
        self.features = {}
        self.labels = {}

        self.features[Word(0,0, 1, "NONE")] = 0

    def load(self):
        files = os.listdir(self.folder)
        for filename in files:
            path = os.path.join(self.folder, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                sentenceList = self.reader.read_text(content)
                for sentence in sentenceList:
                    self.sentences.append(sentence)

    def build(self):
        for sentence in self.sentences:
            for word in sentence.words:
                self.features[word] = len(self.features)
                for label in sentence.word_labels[word]:
                    self.labels[label] = len(self.labels)


    def get(self, sentence_index):
        sentence = self.sentences[sentence_index]
        word_vectors = sentence.vectorize_words(self.features)
        label_vectors = sentence.vectorize_words(self.labels)
        (word_vectors, label_vectors)
    
    def get_all(self):
        list = []
        for i in range(0, len(self.sentences)):
            tuple = self.get(i)
            list.append(tuple)
        return list
    
if __name__ == "__main__":
    dataset = Dataset('resources/')
    dataset.load()