import json

from pyhanlp import CustomDictionary
from pyhanlp import HanLP


def add_to_dictionary(word, part, mod=0):
    result = CustomDictionary.add(word, part)
    if not result and mod:
        CustomDictionary.insert(word, part)
    text = "我用天猫交社保"
    print(HanLP.segment(text))
    return result


if __name__ == "__main__":
    # add_to_dictionary("社保", 'entity', 1)
    # add_to_dictionary("交", 'event', 1)
    HanLP.Config.enableDebug()
    file = open(r'..\..\resource\eg8.txt', encoding='utf-8')
    file_write = open(r'..\..\resource\词性.txt', "w", encoding='utf-8')
    text = file.read()
    text_list = text.split("\n")
    for item in text_list:
        reslut = HanLP.segment(item)
        reslut_json_str = json.loads(
            str(reslut).replace('[', '{"').replace(']', '"}').replace('/', '":"').replace(',', '","'))
        for k, v in reslut_json_str.items():
            file_path = r'..\..\resource\词性'+v[0]+'.txt'
            file_word = open(file_path, "a", encoding='utf-8')
            print(k, ':', v, file=file_word)
        print(reslut_json_str, file=file_write)
