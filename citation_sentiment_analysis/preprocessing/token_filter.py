import pandas as pd
import nltk

from ..datasets.words_en import download_and_read_english_words
from ..utils.string import lower_all


def get_words_to_exclude():
    # Note: may not be used anymore
    return set(nltk.corpus.stopwords.words('english')) - set([
        "but", "while", "against", "before", "after", "just", "don", 
        "don't", "should", "should've", "no", "nor", "not",
        "ain", "aren", "aren't", "couldn", "couldn't", "didn",
        "didn't", "doesn", "doesn't", "hadn", "hadn't", "hasn",
        "hasn't", "haven", "haven't", "isn", "isn't", "ma",
        "mightn", "mightn't", "mustn", "mustn't", "needn", 
        "needn't", "shan", "shan't", "shouldn", "shouldn't",
        "wasn", "wasn't", "weren", "weren't", "won"," won't",
        "wouldn", "wouldn't"
    ])


def get_default_words_to_include():
    return {
        t for t in download_and_read_english_words() if len(t) > 2
    } | {'no'}


def keep_sentence_list_tokens_in(sentence_list_tokens, tokens_to_include):
    if not isinstance(tokens_to_include, set):
        tokens_to_include = set(tokens_to_include)
    return [
        [t for t in lower_all(tokens) if t in tokens_to_include]
        for tokens in sentence_list_tokens
    ]


def get_feature_names(X):
    return X._get_feature_names()


def get_token_counts(tokens):
    return pd.Series(list(tokens)).to_frame('token').groupby('token').size().sort_values(ascending=False)


def drop_token_counts_where(token_counts, fn=None):
    feature_names = get_feature_names(token_counts)
    token_count_sum = pd.Series(token_counts.sum(axis=0).tolist()[0], index=feature_names)
    token_columns = pd.Series(range(token_counts.shape[1]), index=feature_names)
    columns_to_keep = fn(token_count_sum).index
    filtered_counts = token_counts[:, (
        token_columns[columns_to_keep]
    )]
    filtered_counts._get_feature_names = lambda: list(columns_to_keep)
    return filtered_counts


def drop_token_counts_less_than(token_counts, min_count):
    return drop_token_counts_where(
        token_counts, lambda token_count_sum: token_count_sum[token_count_sum > min_count]
    )


def drop_token_counts_not_in_top(token_counts, top_count):
    return drop_token_counts_where(
        token_counts, lambda token_count_sum: token_count_sum.sort_values(ascending=False)[:top_count]
    )
