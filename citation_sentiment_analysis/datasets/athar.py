import os
from pathlib import Path
from zipfile import ZipFile

import pandas as pd

from ..utils.download import download_if_not_exists


athar_corpus_download_url = (
  'http://cl.awaisathar.com/citation-sentiment-corpus/citation_sentiment_corpus.zip'
)

data_path = 'data'
athar_corpus_zip = os.path.join(data_path, 'athar/citation_sentiment_corpus.zip')
athar_corpus_txt = os.path.join(data_path, 'athar/citation_sentiment_corpus.txt')


def download_and_extract_athar_corpus_if_not_exists():
    download_if_not_exists(athar_corpus_download_url, athar_corpus_zip)
    if not os.path.exists(athar_corpus_txt):
        os.makedirs(os.path.dirname(athar_corpus_txt), exist_ok=True)
        with ZipFile(athar_corpus_zip) as zf:
            assert len(zf.namelist()) == 1
            with zf.open(zf.namelist()[0]) as txt_f:
                Path(athar_corpus_txt).write_bytes(txt_f.read())

def read_athar_txt():
    return pd.read_csv(
        athar_corpus_txt,
        sep = '\t', 
        names = ["source_paper_id", "target_paper_id", "sentiment", "citation_text"],
        skiprows = 18
    )


def download_and_read_athar_txt():
    download_and_extract_athar_corpus_if_not_exists()
    return read_athar_txt()


def to_athar_sentiment_label(sentiment):
    # create a more readable sentiment label
    return sentiment.map({
        'o': 'neutral', 'p': 'positive', 'n': 'negative'
    })


def download_and_read_athar_txt_with_sentiment_label():
    df = download_and_read_athar_txt()
    df['sentiment_label'] = to_athar_sentiment_label(df['sentiment'])
    return df


def get_athar_sentence_lengths(df):
    return df['citation_text'].str.len()


def sort_athar_by_sentence_lengths(df, sentence_lengths=None):
    if sentence_lengths is None:
        sentence_lengths = get_athar_sentence_lengths(df)
    return df.reindex(sentence_lengths.sort_values().index)


def filter_long_sentences_from_athar(df, sentence_lengths=None, threshold=1000):
    if sentence_lengths is None:
        sentence_lengths = get_athar_sentence_lengths(df)
    return df[sentence_lengths <= threshold]
