# -*- coding: utf-8 -*-
# author: cgcel

import re
import zipfile
from datetime import datetime

import opencc
from tqdm import tqdm


# 通过 opencc 繁体转简体
def trans_to_simp(input_data: str):
    converter = opencc.OpenCC('t2s.json')
    output_data = converter.convert(input_data)
    return output_data


# 通过正则匹配自定义短语
def find_words(input_data: str):
    pattern = re.compile(r'(.*?)\t(.*?)\t')
    result = pattern.findall(input_data)
    return result


# 生成 gboard 格式词典
def generate_gboardDic(words_list: list):
    with open("dictionary.txt", "w+", encoding="utf-8") as f: # 覆盖写入
        f.write("# Gboard Dictionary version:1\n")
        for word in words_list:
            f.write(word)
    
    zf = zipfile.ZipFile("PersonalDictionary-{}.zip".format(datetime.now().strftime("%Y%m%d%H%M%S")),
                         mode="w",
                         compression=zipfile.ZIP_DEFLATED)
    zf.write("dictionary.txt")
    zf.close()

def main():
    # 获取 rime userdb.txt 用户词典
    rime_userdb_path = input("rime_userdb_path: ")
    with open(rime_userdb_path, encoding="utf-8") as f:
        userdb_data = f.read()

    # (可选)将繁体字的userdb.txt内容转成简体字
    userdb_data = trans_to_simp(userdb_data)

    # 匹配自定义短语
    words_list = find_words(userdb_data)

    # 新建列表存储短语
    new_words_list = []
    for word in tqdm(words_list):
        new_word = '{}\t{}\tzh-CN\n'.format(word[0], word[1])
        new_words_list.append(new_word)

    # 生成 gboard 个人词典
    generate_gboardDic(words_list=new_words_list)


if __name__ == '__main__':
    main()
