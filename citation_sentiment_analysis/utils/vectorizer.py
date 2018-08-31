from sklearn.feature_extraction.text import CountVectorizer


def transform_to_counts(X):
    vectorizer = CountVectorizer(tokenizer=lambda X: X, lowercase=False)
    X_count = vectorizer.fit_transform(X)
    X_count._get_feature_names = vectorizer.get_feature_names
    return X_count
