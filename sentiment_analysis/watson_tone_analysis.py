from watson_developer_cloud import ToneAnalyzerV3
import json

tone_analyzer = ToneAnalyzerV3(
    username='b6ae0afa-7e16-41c3-a129-370c2988e5a1',
    password='zX3HYxJoWyqN',
    version='2016-05-19')

reagan_tone = open("candidates/reagan/reagan_speeches.txt", encoding="utf8").read()

clinton_tone = open("candidates/clinton/clinton_speeches.txt", encoding="utf8").read()

print(tone_analyzer.tone(reagan_tone))
print(tone_analyzer.tone(clinton_tone))
