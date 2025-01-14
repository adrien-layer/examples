# Spam Detection Project Example

from typing import Any
from layer import Featureset, Train
from sklearn.feature_extraction.text import TfidfVectorizer


def train_model(train: Train, sf: Featureset("sms_featureset")) -> Any:
    data = sf.to_pandas()

    # Transform text data
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_vectorizer.fit(data["clean_message"])

    return tfidf_vectorizer

