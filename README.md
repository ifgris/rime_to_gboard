# RimeToGboardDictionary

## 简介

本脚本可将 Rime `xxx.userdb.txt` (测试于 [Weasel](https://github.com/rime/weasel)) 转换为 Gboard `PersonalDictionary.zip` 格式, 便于将词库导入 gboard.

## 脚本依赖

- Python 3.10.9
- OpenCC 1.1.1
- tqdm 4.64.1

## 使用方法

1. 安装 python 以及依赖:

    ```shell
    pip install -r requirements.txt
    ```

2. (可选) userdb.txt 文件内容是 rime 默认为繁体中文, 如果是简体中文的 userdb.txt, 则需注释一行代码 `userdb_data = trans_to_simp(userdb_data)`:

    ```python
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
    ```

3. 运行脚本, 按照提示将你的待转换的 `userdb.txt` 拖拽入命令行.

4. 回车, 等待数秒, `.zip` 压缩文件将自动生成.

5. 将 `.zip` 压缩文件导入手机存储中, 在 gboard 设置 - 字典 - 个人字典 - 中文 (简体) - 点击右上角 *导入* - 选择 `.zip` 压缩文件.
