import json

from pyhanlp import *

# 共性分析
Occurrence = JClass("com.hankcs.hanlp.corpus.occurrence.Occurrence")
PairFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.PairFrequency")
TermFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.TermFrequency")
TriaFrequency = JClass("com.hankcs.hanlp.corpus.occurrence.TriaFrequency")

file = open(r'..\..\resource\0527-0716.txt', encoding='utf-8')
text = file.read()
occurrence = Occurrence()
occurrence.addAll(text)
occurrence.compute()


def level_one():
    print("\t\t词频统计")
    unigram = occurrence.getUniGram()
    all_dics = []
    for entry in unigram.iterator():
        term_frequency = str(entry.getValue())
        term_frequency = term_frequency.split('=')
        dic = {"word": term_frequency[0], "times": int(term_frequency[1])}
        all_dics.append(dic)
    all_dics.sort(key=lambda x: x["times"], reverse=True)
    file_one = open(r'..\..\resource\一阶.txt', "w", encoding='utf-8')
    for word in all_dics:
        print(word["word"], " = ", word["times"], file=file_one)
    print('end')


def level_two():
    print("\t\t二阶共性")
    bigram = occurrence.getBiGram()
    all_dics = []
    for entry in bigram.iterator():
        pair_frequency = entry.getValue()
        if pair_frequency.isRight():
            pair_frequency = str(pair_frequency)
            pair_frequency = '{"key":"'+pair_frequency.replace('= ', '","').replace('=', '":').replace(" ", ', "')+'}'
            dic = json.loads(pair_frequency)
            all_dics.append(dic)
    all_dics.sort(key=lambda x: x["mi"], reverse=True)
    file_two = open(r'..\..\resource\二阶.txt', "w", encoding='utf-8')
    for word in all_dics:
        print(word, file=file_two)
    print('end')


def level_three():
    print("\t\t三阶共性")
    trigram = occurrence.getTriGram()
    all_dics = []
    for entry in trigram.iterator():
        tria_frequency = entry.getValue()
        if tria_frequency.isRight():
            tria_frequency = str(tria_frequency)
            tria_frequency = '{"key":"'+tria_frequency.replace('= ', '","').replace('=', '":').replace(" ", ', "')+'}'
            dic = json.loads(tria_frequency)
            all_dics.append(dic)
    all_dics.sort(key=lambda x: x["tf"], reverse=True)
    file_three = open(r'..\..\resource\三阶.txt', "w", encoding='utf-8')
    for word in all_dics:
        print(word, file=file_three)
    print('end')


if __name__ == "__main__":
    level_one()
    level_two()
    level_three()
