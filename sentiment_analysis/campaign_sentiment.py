import json

from sentiment_analysis import speech_sentiment_module as speech

# 1932 candidates
# Franklin Roosevelt
roosevelt = open("candidates/roosevelt/roosevelt_speeches.txt", encoding="utf8").read()

roosevelt_top_words = speech.frequency_filter(roosevelt)
print("roosevelt:", roosevelt_top_words)

with open('json_data/roosevelt_top_words.json', 'w') as fp:
    json.dump(roosevelt_top_words, fp)

roosevelt_sentence_decisions = speech.sentence_sentiment(roosevelt)
roosevelt_sentiment_decisions = speech.overall_sentiment(roosevelt_sentence_decisions)
print("roosevelt:", roosevelt_sentiment_decisions)

with open('json_data/roosevelt_sentiment_decisions.json', 'w') as t:
    json.dump(roosevelt_sentiment_decisions, t)


# # Herbert Hoover
# hoover = open("candidates/hoover/hoover_speeches.txt", encoding="utf8").read()
#
# hoover_top_words = speech.frequency_filter(hoover)
# print("hoover:", hoover_top_words)
#
# hoover_sentence_decisions = speech.sentence_sentiment(hoover)
# hoover_sentiment_decisions = speech.overall_sentiment(hoover_sentence_decisions)
# print("hoover:", hoover_sentiment_decisions)
#
# # 1960 candidates\
# # Robert Nixon
# nixon = open("candidates/nixon/nixon_speeches.txt", encoding="utf8").read()
#
# nixon_top_words = speech.frequency_filter(nixon)
# print("nixon:", nixon_top_words)
#
# nixon_sentence_decisions = speech.sentence_sentiment(nixon)
# nixon_sentiment_decisions = speech.overall_sentiment(nixon_sentence_decisions)
# print("nixon:", nixon_sentiment_decisions)
#
# # John Kennedy
# kennedy = open("candidates/kennedy/kennedy_speeches.txt", encoding="utf8").read()
#
# kennedy_top_words = speech.frequency_filter(kennedy)
# print("kennedy:", kennedy_top_words)
#
# kennedy_sentence_decisions = speech.sentence_sentiment(kennedy)
# kennedy_sentiment_decisions = speech.overall_sentiment(kennedy_sentence_decisions)
# print("kennedy:", kennedy_sentiment_decisions)
#
# # 1980 candidates
# # Ronald Reagan
# reagan = open("candidates/reagan/reagan_speeches.txt", encoding="utf8").read()
#
# reagan_top_words = speech.frequency_filter(reagan)
# print("reagan:", reagan_top_words)
#
# reagan_sentence_decisions = speech.sentence_sentiment(reagan)
# reagan_sentiment_decisions = speech.overall_sentiment(reagan_sentence_decisions)
# print("reagan:", reagan_sentiment_decisions)
#
# # Jimmy Carter
# carter = open("candidates/carter/carter_speeches.txt", encoding="utf8").read()
#
# carter_top_words = speech.frequency_filter(carter)
# print("carter:", carter_top_words)
#
# carter_sentence_decisions = speech.sentence_sentiment(carter)
# carter_sentiment_decisions = speech.overall_sentiment(carter_sentence_decisions)
# print("carter:", carter_sentiment_decisions)
#
# # 2008 candidates
# # John McCain
# mccain = open("candidates/mccain/mccain_speeches.txt", encoding="utf8").read()
#
# mccain_top_words = speech.frequency_filter(mccain)
# print("mccain:", mccain_top_words)
#
# mccain_sentence_decisions = speech.sentence_sentiment(mccain)
# mccain_sentiment_decisions = speech.overall_sentiment(mccain_sentence_decisions)
# print("mccain:", mccain_sentiment_decisions)
#
# # Barack Obama
# obama = open("candidates/obama/obama_speeches.txt", encoding="utf8").read()
#
# obama_top_words = speech.frequency_filter(obama)
# print("obama:", obama_top_words)
#
# obama_sentence_decisions = speech.sentence_sentiment(obama)
# obama_sentiment_decisions = speech.overall_sentiment(obama_sentence_decisions)
# print("obama:", obama_sentiment_decisions)
#
# # 2016 candidates
# # Donald Trump
# trump = open("candidates/trump/trump_speeches.txt", encoding="utf8").read()
#
# trump_top_words = speech.frequency_filter(trump)
# print("trump:", trump_top_words)
#
# trump_sentence_decisions = speech.sentence_sentiment(trump)
# trump_sentiment_decisions = speech.overall_sentiment(trump_sentence_decisions)
# print("trump:", trump_sentiment_decisions)
#
# # Hillary Clinton
# clinton = open("candidates/clinton/clinton_speeches.txt", encoding="utf8").read()
#
# clinton_top_words = speech.frequency_filter(clinton)
# print("clinton:", clinton_top_words)
#
# clinton_sentence_decisions = speech.sentence_sentiment(clinton)
# clinton_sentiment_decisions = speech.overall_sentiment(clinton_sentence_decisions)
# print("clinton:", clinton_sentiment_decisions)
#
# # Wildcards
# # Al Gore
# gore = open("candidates/gore/gore_speeches.txt", encoding="utf8").read()
#
# gore_top_words = speech.frequency_filter(gore)
# print("gore:", gore_top_words)
#
# gore_sentence_decisions = speech.sentence_sentiment(gore)
# gore_sentiment_decisions = speech.overall_sentiment(gore_sentence_decisions)
# print("gore:", gore_sentiment_decisions)
#
# # Bernie Sanders
# sanders = open("candidates/sanders/sanders_speeches.txt", encoding="utf8").read()
#
# sanders_top_words = speech.frequency_filter(sanders)
# print("sanders:", sanders_top_words)
#
# sanders_sentence_decisions = speech.sentence_sentiment(sanders)
# sanders_sentiment_decisions = speech.overall_sentiment(sanders_sentence_decisions)
# print("sanders:", sanders_sentiment_decisions)
