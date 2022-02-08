# Creates frequency.csv of names from names.txt against documents

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

vocabulary = [line.strip() for line in open('names.txt').readlines()]
# last names
names = [words.split()[-1] for words in vocabulary]
names = [name.lower() for name in names]


def create_corpus(start, end):
    # get each word
    documents = []
    i = start
    while (i < end+1):
        file = "{}.txt".format(i)
        corpus = open(file).read()
        documents.append(corpus)
        i += 1
    return documents


if __name__ == "__main__":
    # set the file number to start from and end on
    start = 29
    end = 36
    
    documents = create_corpus(start, end)
    vectorizer = CountVectorizer(min_df=1, vocabulary=names)
    words_matrix = vectorizer.fit_transform(documents)
    df = pd.DataFrame(data=words_matrix.todense(), 
                    index=('document_%s' % (i+start) for i in range(words_matrix.shape[0])),
                    columns=vectorizer.vocabulary_)
    df.index.name = 'id'
    df.to_csv('frequency.csv')
