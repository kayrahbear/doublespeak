import speech_sentiment_module as speech

# 1932 candidates
# Franklin Roosevelt
roosevelt = open("candidates/roosevelt/roosevelt_speeches.txt", encoding="utf8").read()

roosevelt_top_words = speech.frequency_filter(roosevelt)
roosevelt_top_words_list = ', '.join(roosevelt_top_words)
print("roosevelt:", roosevelt_top_words_list)

# roosevelt_sentence_decisions = speech.sentence_sentiment(roosevelt)
# roosevelt_sentiment_decisions = speech.overall_sentiment(roosevelt_sentence_decisions)
# print("roosevelt:", roosevelt_sentiment_decisions)

# Herbert Hoover
hoover = open("candidates/hoover/hoover_speeches.txt", encoding="utf8").read()

hoover_top_words = speech.frequency_filter(hoover)
hoover_top_words_list = ', '.join(hoover_top_words)
print("hoover:", hoover_top_words_list)

# hoover_sentence_decisions = speech.sentence_sentiment(hoover)
# hoover_sentiment_decisions = speech.overall_sentiment(hoover_sentence_decisions)
# print("hoover:", hoover_sentiment_decisions)

# 1960 candidates\
# Robert Nixon
nixon = open("candidates/nixon/nixon_speeches.txt", encoding="utf8").read()

nixon_top_words = speech.frequency_filter(nixon)
nixon_top_words_list = ', '.join(nixon_top_words)
print("nixon:", nixon_top_words_list)

# nixon_sentence_decisions = speech.sentence_sentiment(nixon)
# nixon_sentiment_decisions = speech.overall_sentiment(nixon_sentence_decisions)
# print("nixon:", nixon_sentiment_decisions)

# John Kennedy
kennedy = open("candidates/kennedy/kennedy_speeches.txt", encoding="utf8").read()

kennedy_top_words = speech.frequency_filter(kennedy)
kennedy_top_words_list = ', '.join(kennedy_top_words)
print("kennedy:", kennedy_top_words_list)

# kennedy_sentence_decisions = speech.sentence_sentiment(kennedy)
# kennedy_sentiment_decisions = speech.overall_sentiment(kennedy_sentence_decisions)
# print("kennedy:", kennedy_sentiment_decisions)

# 1980 candidates
# Ronald Reagan
reagan = open("candidates/reagan/reagan_speeches.txt", encoding="utf8").read()

reagan_top_words = speech.frequency_filter(reagan)
reagan_top_words_list = ', '.join(reagan_top_words)
print("reagan:", reagan_top_words_list)

# reagan_sentence_decisions = speech.sentence_sentiment(reagan)
# reagan_sentiment_decisions = speech.overall_sentiment(reagan_sentence_decisions)
# print("reagan:", reagan_sentiment_decisions)

# Jimmy Carter
carter = open("candidates/carter/carter_speeches.txt", encoding="utf8").read()

carter_top_words = speech.frequency_filter(carter)
carter_top_words_list = ', '.join(carter_top_words)
print("carter:", carter_top_words_list)

# carter_sentence_decisions = speech.sentence_sentiment(carter)
# carter_sentiment_decisions = speech.overall_sentiment(carter_sentence_decisions)
# print("carter:", carter_sentiment_decisions)

# 2008 candidates
# John McCain
mccain = open("candidates/mccain/mccain_speeches.txt", encoding="utf8").read()

mccain_top_words = speech.frequency_filter(mccain)
mccain_top_words_list = ', '.join(mccain_top_words)
print("mccain:", mccain_top_words_list)

# mccain_sentence_decisions = speech.sentence_sentiment(mccain)
# mccain_sentiment_decisions = speech.overall_sentiment(mccain_sentence_decisions)
# print("mccain:", mccain_sentiment_decisions)

# Barack Obama
obama = open("candidates/obama/obama_speeches.txt", encoding="utf8").read()

obama_top_words = speech.frequency_filter(obama)
obama_top_words_list = ', '.join(obama_top_words)
print("obama:", obama_top_words_list)

# obama_sentence_decisions = speech.sentence_sentiment(obama)
# obama_sentiment_decisions = speech.overall_sentiment(obama_sentence_decisions)
# print("obama:", obama_sentiment_decisions)

# 2016 candidates
# Donald Trump
trump = open("candidates/trump/trump_speeches.txt", encoding="utf8").read()

trump_top_words = speech.frequency_filter(trump)
trump_top_words_list = ', '.join(trump_top_words)
print("trump:", trump_top_words_list)
# trump_sentence_decisions = speech.sentence_sentiment(trump)
# trump_sentiment_decisions = speech.overall_sentiment(trump_sentence_decisions)
# print("trump:", trump_sentiment_decisions)

# Hillary Clinton
clinton = open("candidates/clinton/clinton_speeches.txt", encoding="utf8").read()

clinton_top_words = speech.frequency_filter(clinton)
clinton_top_words_list = ', '.join(clinton_top_words)
print("clinton:", clinton_top_words_list)

# clinton_sentence_decisions = speech.sentence_sentiment(clinton)
# clinton_sentiment_decisions = speech.overall_sentiment(clinton_sentence_decisions)
# print("clinton:", clinton_sentiment_decisions)

# Wildcards
# Al Gore
gore = open("candidates/gore/gore_speeches.txt", encoding="utf8").read()

gore_top_words = speech.frequency_filter(gore)
gore_top_words_list = ', '.join(gore_top_words)
print("gore:", gore_top_words_list)

# gore_sentence_decisions = speech.sentence_sentiment(gore)
# gore_sentiment_decisions = speech.overall_sentiment(gore_sentence_decisions)
# print("gore:", gore_sentiment_decisions)

# Bernie Sanders
sanders = open("candidates/sanders/sanders_speeches.txt", encoding="utf8").read()

sanders_top_words = speech.frequency_filter(sanders)
sanders_top_words_list = ', '.join(sanders_top_words)
print("sanders:", sanders_top_words_list)

# sanders_sentence_decisions = speech.sentence_sentiment(sanders)
# sanders_sentiment_decisions = speech.overall_sentiment(sanders_sentence_decisions)
# print("sanders:", sanders_sentiment_decisions)
