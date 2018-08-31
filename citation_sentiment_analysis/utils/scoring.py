import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.scorer import check_scoring


# similar to cross_val_score but only checks one split
def train_test_score(
    model, X, y, train_test_ratio=0.25, scoring='accuracy', shuffle=True, random_state=None,
    train_test_split_fn=None):

    if train_test_split_fn is None:
        train_test_split_fn = train_test_split
    scorer = check_scoring(model, scoring)
    X_train, X_test, y_train, y_test = train_test_split_fn(
        X, y, test_size=train_test_ratio, shuffle=shuffle, random_state=random_state
    )
    print('shapes:', [x.shape for x in [X_train, X_test, y_train, y_test]])
    print('y_train:', pd.Series(y_train).value_counts().to_dict())
    print('y_test:', pd.Series(y_test).value_counts().to_dict())
    model.fit(X_train, y_train)
    return scorer(model, X_test, y_test)
