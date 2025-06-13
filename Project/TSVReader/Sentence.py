from _collections import defaultdict


class Sentence:

    def __init__(self, index, text):
        self.index = index
        self.text = text
        self.words = []
        self.labels = defaultdict(list)
        self.word_labels = defaultdict(list)
        self.level_size = 5

    def add_word(self, word):
        self.words.append(word)

    def add_word_label(self, word, label):
        self.labels[label].append(word)
        self.word_labels[word].append(label)

    def __str__(self):
        return self.text
    
    def vectorize_words(self, dictionary):
        vector_list = []
        for word in self.words:
            index = 0
            if word in dictionary:
                index = dictionary[word]

            vector = [0.0] * len(dictionary)
            vector[index] = 1.0
            vector_list.append(vector)
        
        return vector_list

    def vectorize_labels(self, dictionary):
        vector_list = []
        for word in self.words:
            index = 0
            vector = [0.0] * self.level_size * len(dictionary)
            
            for level, label in enumerate(self.word_labels[word]):
                dictionary_index = dictionary[label]
                index = level * len(dictionary) + dictionary_index
                vector[index] = 1.0
            
            vector_list.append(vector)

        return vector_list