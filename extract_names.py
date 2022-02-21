# Creates frequency.csv of names from names.txt against documents

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import os


def getlastnames(filename):
    # alphabetical
    df = pd.read_csv(filename)
    names = df['lastname'].dropna()
    names = [name.lower() for name in names]
    names = set(names)
    return names
        

def create_corpus(files):
    # get each word
    documents = []
    for file in files:
        text = open("./data_txts/"+file).read()
        documents.append(text)
    return documents

def write_csv(csv, names, documents):
    vectorizer = CountVectorizer(min_df=1, vocabulary=names)
    words_matrix = vectorizer.fit_transform(documents)
    df = pd.DataFrame(data=words_matrix.todense(), 
                    index=(i for i in range(len(documents))),
                    columns=vectorizer.vocabulary_)
    df.index.name = 'id'
    df.to_csv(csv)


if __name__ == "__main__":
    names = getlastnames("names.csv")

    # all files in data texts
    files = os.listdir("./data_txts")
    documents = create_corpus(files)

    write_csv("frequency.csv", names, documents)