# -*- coding: utf-8 -*-
# author: cgcel

import re
import zipfile
from datetime import datetime

import opencc
from tqdm import tqdm


# 获取 rime userdb.txt 用户词典
def read_file(rime_userdb_path: str):
    userdb_data = []
    with open(rime_userdb_path, encoding="utf-8") as f:
        for line in tqdm(f, total=sum(1 for _ in open(rime_userdb_path, "r", encoding="utf-8")), desc="读取 userdb.txt 文件"):
            userdb_data.append(line)
    return userdb_data


# 通过 opencc 繁体转简体
def trans_to_simp(input_data: list):
    output_data = []
    converter = opencc.OpenCC('t2s.json')
    for item in tqdm(input_data, desc="opencc 繁体转简体"):
        output_data.append(converter.convert(item))
    return output_data

# 通过 opencc 简体转繁体
def simp_to_trans(input_data: list):
    output_data = []
    converter = opencc.OpenCC('s2t.json')
    for item in tqdm(input_data, desc="opencc 简体转繁体"):
        output_data.append(converter.convert(item))
    return output_data


# 通过正则匹配自定义短语
def find_words(input_data: list):
    result = []
    pattern = re.compile(r'(.*?)\t(.*?)\t')
    for line in tqdm(input_data, desc="正则匹配短语"):
        res = pattern.findall(line)
        result.append(res)
    return result


# 新建列表存储短语
def generate_gboard_format_data(words_list: list):
    new_words_list = []
    for word in tqdm(words_list, desc="创建转换格式短语列表"):
        if word != []:
            new_word = '{}\t{}\tzh-CN\n'.format(word[0][0], word[0][1])
            new_words_list.append(new_word)
    return new_words_list


# 生成 gboard 格式词典
def generate_gboardDic(words_list: list):
    with open("dictionary.txt", "w+", encoding="utf-8") as f:  # 覆盖写入
        f.write("# Gboard Dictionary version:1\n")
        for word in tqdm(words_list, desc="写入 dictionary.txt"):
            f.write(word)

    zf = zipfile.ZipFile("PersonalDictionary-{}.zip".format(datetime.now().strftime("%Y%m%d%H%M%S")),
                         mode="w",
                         compression=zipfile.ZIP_DEFLATED)
    zf.write("dictionary.txt")
    zf.close()


def main():
    rime_userdb_path = input("输入 rime_userdb_path: ")

    # 获取 rime userdb.txt 用户词典
    userdb_data = read_file(rime_userdb_path)

    while True:
        input_format = ["0", "1"]
        userdb_type = input("输入 Rime userdb.txt 简繁类型 (0 -- 简体, 1 -- 繁体): ")
        if userdb_type not in input_format:
            userdb_type = print("格式不对, 重新输入")
            continue
        gboard_type = input("输入 Gboard .zip 简繁类型 (0 -- 简体, 1 -- 繁体): ")
        if gboard_type not in input_format:
            gboard_type = print("格式不对, 重新输入")
            continue
        else:
            break

    # 将简体字的userdb.txt内容转成繁体字
    if (userdb_type == "0" and gboard_type == "1"):
        userdb_data = simp_to_trans(userdb_data)

    # 将繁体字的userdb.txt内容转成简体字
    if (userdb_type == "1" and gboard_type == "0"):
        userdb_data = trans_to_simp(userdb_data)

    # 匹配自定义短语
    words_list = find_words(userdb_data)

    # 新建列表存储短语
    new_words_list = generate_gboard_format_data(words_list)

    # 生成 gboard 个人词典
    generate_gboardDic(words_list=new_words_list)


if __name__ == '__main__':
    main()
