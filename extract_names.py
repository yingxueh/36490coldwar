# Creates frequency.csv of names from names.txt against documents

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import os


def sort_names(filename):
    # alphabetical
    newfilename = "sorted_names.txt"
    file = open(filename)
    newfile = open(newfilename, "w")
    data=file.readlines()
    s = set(data)
    data=list(s)
    data.sort()
    for name in data:
        newfile.write(name)
    return newfilename
        

def create_corpus(files):
    # get each word
    documents = []
    for file in files:
        text = open("./data_txts/"+file).read()
        documents.append(text)
    return documents


if __name__ == "__main__":
    newfilename = sort_names("names.txt")
    vocabulary = [line.strip() for line in open(newfilename).readlines()]
    # last names
    names = [words.split()[-1] for words in vocabulary]
    names = [name.lower() for name in names]
    names = set(names)

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