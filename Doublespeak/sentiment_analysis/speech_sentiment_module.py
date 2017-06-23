import string
from statistics import mean

from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize, sent_tokenize

import sentiment_module as s

stop_words = stopwords.words("english")
punctuation = list(string.punctuation)


def sentence_sentiment(data_set):
    speech_sentences = sent_tokenize(data_set)
    decisions = []
    for sentence in speech_sentences:
        sentiment = s.sentiment(sentence)
        decisions.append(sentiment)
    return decisions


def frequency_filter(data_set):
    words = word_tokenize(data_set)
    no_capitals = list([word.lower() for word in words])
    filtered = [word for word in no_capitals if word not in stop_words]
    no_punct = [word for word in filtered if word not in punctuation]
    frequency = FreqDist(no_punct)
    top_fifty_words = frequency.most_common(50)
    top_twenty_just_words, top_word_count = map(list, zip(*top_fifty_words))
    top_twenty_just_words = [word for word in top_twenty_just_words if len(word) > 4]
    return top_twenty_just_words[:20]


def overall_sentiment(sentiment_decisions):
    sentiment_postitive_or_negative, sentiment_confidence_percent = map(list, zip(*sentiment_decisions))
    sentiment_frequency = FreqDist(sentiment_postitive_or_negative)
    winning_sentiment = sentiment_frequency.most_common(2)
    confidence_frequency = mean(sentiment_confidence_percent) * 100
    return winning_sentiment, confidence_frequency

