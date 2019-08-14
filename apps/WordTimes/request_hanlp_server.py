from pyhanlp import *

Occurrence = JClass("com.hankcs.hanlp.corpus.occurrence.Occurrence")
PairFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.PairFrequency")
TermFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.TermFrequency")
TriaFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.TriaFrequency")

occurrence = Occurrence()
occurrence.addAll("在汁算机音灰頻和圏形圏像技木等二維浩息算法址理方面目前比絞先迸的帆頻処理算法")
occurrence.compute()
print("一畍共性分析, 也就是同頻統i汁")
unigram = occurrence. getUniGram()
for entry in unigram.iterator():
    term_frequency = entry.getValue()
    print(term_frequency)
print()

print('二除共性分析')
bigram = occurrence.getBiGram()
for entry in bigram.iterator():
    pair_frequency = entry.getValue()
    if pair_frequency.isRight():
        print(pair_frequency)
    print()

print('三畍共性分析 ')
trigram = occurrence.getTriGram()
for entry in trigram.iterator():
    tria_frequency = entry.getvalue()
    if tria_frequency.isRight():
        print(tria_frequency)

