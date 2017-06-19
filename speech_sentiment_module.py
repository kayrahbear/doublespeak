import sentiment_module as s
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string

stop_words = stopwords.words("english")
punctuation = list(string.punctuation)


def sentences_filter(data_set):
    sentences = sent_tokenize(data_set)
    return sentences


def sentance_sentiment(speech_sentances):
    decisions = []
    for c in speech_sentances:
        sentiment = s.sentiment(c)
        decisions.append(sentiment)
    return decisions


def frequency_filter(data_set):
    words = word_tokenize(data_set)
    no_capitals = list([word.lower() for word in words])
    filtered = [word for word in no_capitals if word not in stop_words]
    no_punct = [word for word in filtered if word not in punctuation]
    frequency = FreqDist(no_punct)
    top_fifteen_words = frequency.most_common(25)
    return top_fifteen_words


def overall_sentiment(sentiment_decisions):
    sentiment_frequency = FreqDist(sentiment_decisions)
    winning_sentiment = sentiment_frequency.most_common(1)
    return winning_sentiment


# testing! testing! 1 2 3

ronald_reagan = open("candidates/reagan/reagan_speeches.txt", encoding="utf8")
ronald_reagan = ronald_reagan.read()

print(frequency_filter(ronald_reagan))

filtered = sentences_filter(ronald_reagan)

sentiment_decisions = sentance_sentiment(filtered)

print(overall_sentiment(sentiment_decisions))
