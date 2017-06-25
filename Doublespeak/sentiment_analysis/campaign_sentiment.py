import speech_sentiment_module as speech

file_names = ["candidates/carter_speeches.txt", "candidates/clinton_speeches.txt", "candidates/gore_speeches.txt",
              "candidates/hoover_speeches.txt", "candidates/kennedy_speeches.txt", "candidates/nixon_speeches.txt",
              "candidates/mccain_speeches.txt", "candidates/obama_speeches.txt", "candidates/reagan_speeches.txt",
              "candidates/roosevelt_speeches.txt", "candidates/sanders_speeches.txt", "trump_speeches.txt"]


def analyze_speech(filename):
    candidate = open(filename, encoding='utf8').read()
    candidate_top_words = speech.frequency_filter(candidate)
    candidate_top_words_list = ', '.join(candidate_top_words)
    sentence_decisions = speech.sentence_sentiment(candidate)
    sentiment_decision = speech.overall_sentiment(sentence_decisions)
    return candidate_top_words_list, sentiment_decision


for file in file_names:
    analyzed_speech = analyze_speech(file)
    print(file, analyzed_speech)

