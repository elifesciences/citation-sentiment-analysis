import sys

from tqdm import tqdm

from .word_similarity import most_similar


def simplify_tokens(tokens, token_counts, w2v, threshold=0.60, count_threshold=None, progress=False):
    def get_token_count(token):
        try:
            return token_counts[token]
        except KeyError:
            return 0

    if count_threshold is None:
        count_threshold = token_counts.mean()
    w2v = w2v.loc[w2v.index.intersection(set(token_counts.index) | set(tokens))]
    valid_tokens = set(w2v.index.intersection(tokens).values)

    def _simplify_token(token):
        if token not in valid_tokens:
            return token
        token_count = get_token_count(token)
        if token_count >= count_threshold:
            return token
        token_similarities = most_similar(w2v, token, threshold=threshold, limit=100)
        token_similarities_with_count = ((t, s, get_token_count(t)) for t, s in token_similarities)
        token_similarities_with_count_with_higher_counts = list(
            (t, s, c) for t, s, c in token_similarities_with_count if c > token_count
        )
        if token_similarities_with_count_with_higher_counts:
            return _simplify_token(
                token_similarities_with_count_with_higher_counts[0][0]
            )
        else:
            return token

    if progress:
        tokens = tqdm(tokens, leave=False, file=sys.stdout)
    return (_simplify_token(token) for token in tokens)
