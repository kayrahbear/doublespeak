from watson_developer_cloud import ToneAnalyzerV3
import json

tone_analyzer = ToneAnalyzerV3(
    username='b6ae0afa-7e16-41c3-a129-370c2988e5a1',
    password='zX3HYxJoWyqN',
    version='2016-05-19')

reagan = open("candidates/reagan/reagan_speeches.txt", encoding="utf8").read()
roosevelt = open("candidates/roosevelt/roosevelt_speeches.txt", encoding="utf8").read()
clinton = open("candidates/clinton/clinton_speeches.txt", encoding="utf8").read()
hoover = open("candidates/hoover/hoover_speeches.txt", encoding="utf8").read()
nixon = open("candidates/nixon/nixon_speeches.txt", encoding="utf8").read()
kennedy = open("candidates/kennedy/kennedy_speeches.txt", encoding="utf8").read()
carter = open("candidates/carter/carter_speeches.txt", encoding="utf8").read()
mccain = open("candidates/mccain/mccain_speeches.txt", encoding="utf8").read()
obama = open("candidates/obama/obama_speeches.txt", encoding="utf8").read()
trump = open("candidates/trump/trump_speeches.txt", encoding="utf8").read()
gore = open("candidates/gore/gore_speeches.txt", encoding="utf8").read()
sanders = open("candidates/sanders/sanders_speeches.txt", encoding="utf8").read()

reagan_tone = tone_analyzer.tone(reagan, sentences=False)
with open('json_data/reagan_tone.json', 'w') as fp:
    json.dump(reagan_tone, fp, indent=4)

clinton_tone = tone_analyzer.tone(clinton, sentences=False)
with open('json_data/clinton_tone.json', 'w') as fp:
    json.dump(clinton_tone, fp, indent=4)

roosevelt_tone = tone_analyzer.tone(roosevelt, sentences=False)
with open('json_data/roosevelt_tone.json', 'w') as fp:
    json.dump(roosevelt_tone, fp, indent=4)

hoover_tone = tone_analyzer.tone(hoover, sentences=False)
with open('json_data/hoover_tone.json', 'w') as fp:
    json.dump(hoover_tone, fp, indent=4)

nixon_tone = tone_analyzer.tone(nixon, sentences=False)
with open('json_data/nixon_tone.json', 'w') as fp:
    json.dump(nixon_tone, fp, indent=4)

kennedy_tone = tone_analyzer.tone(kennedy, sentences=False)
with open('json_data/kennedy_tone.json', 'w') as fp:
    json.dump(kennedy_tone, fp, indent=4)

carter_tone = tone_analyzer.tone(carter, sentences=False)
with open('json_data/carter_tone.json', 'w') as fp:
    json.dump(carter_tone, fp, indent=4)

mccain_tone = tone_analyzer.tone(mccain, sentences=False)
with open('json_data/mccain_tone.json', 'w') as fp:
    json.dump(mccain_tone, fp, indent=4)

obama_tone = tone_analyzer.tone(obama, sentences=False)
with open('json_data/obama_tone.json', 'w') as fp:
    json.dump(obama_tone, fp, indent=4)

trump_tone = tone_analyzer.tone(trump, sentences=False)
with open('json_data/trump_tone.json', 'w') as fp:
    json.dump(trump_tone, fp, indent=4)

gore_tone = tone_analyzer.tone(gore, sentences=False)
with open('json_data/gore_tone.json', 'w') as fp:
    json.dump(gore_tone, fp, indent=4)

sanders_tone = tone_analyzer.tone(sanders, sentences=False)
with open('json_data/sanders_tone.json', 'w') as fp:
    json.dump(sanders_tone, fp, indent=4)