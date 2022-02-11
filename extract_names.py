# Creates frequency.csv of names from names.txt against documents

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import os


def create_corpus(files):
    # get each word
    documents = []
    for file in files:
        text = open("./data_txts/"+file).read()
        documents.append(text)
    return documents


if __name__ == "__main__":
    vocabulary = [line.strip() for line in open('names.txt').readlines()]
    # last names
    names = [words.split()[-1] for words in vocabulary]
    names = [name.lower() for name in names]

    # all files in data texts
    files = os.listdir("./data_txts")
    
    documents = create_corpus(files)
    vectorizer = CountVectorizer(min_df=1, vocabulary=names)
    words_matrix = vectorizer.fit_transform(documents)
    df = pd.DataFrame(data=words_matrix.todense(), 
                    index=(file for file in files),
                    columns=vectorizer.vocabulary_)
    df.index.name = 'id'
    df.to_csv('frequency.csv')
