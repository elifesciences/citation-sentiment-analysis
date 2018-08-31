import os
import csv
from zipfile import ZipFile

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from ..utils.download import download_if_not_exists


data_path = 'data'


def load_glove():
    glove_zip = os.path.join(data_path, 'glove.6B.zip')
    download_if_not_exists('http://nlp.stanford.edu/data/glove.6B.zip', glove_zip)
    with ZipFile(glove_zip) as zf:
        with zf.open("glove.6B.50d.txt", "r") as glove_f:
            return pd.read_table(
                glove_f, sep=" ", index_col=0, header=None, quoting=csv.QUOTE_NONE
            ).dropna()


def most_similaries(w2v, tokens, limit=10, threshold=0.0):
    token_vectors = w2v.loc[tokens]
    try:
        similarities = cosine_similarity(
            token_vectors,
            w2v
        )
    except ValueError:
        print('tokens: %s' % tokens)
        raise
    for i, token in enumerate(tokens):
        token_similarities = similarities[i]
        token_index = w2v.index.get_loc(token)
        indices = np.argsort(token_similarities)[::-1][:limit + 1]
        indices = indices[indices != token_index]
        indices = indices[:limit]
        yield [
            (t, s)
            for t, s in zip(w2v.index[indices].values, token_similarities[indices])
            if s >= threshold
        ]


def most_similar(w2v, token, limit=10, threshold=0.0):
    return list(most_similaries(w2v, [token], limit=limit, threshold=threshold))[0]
