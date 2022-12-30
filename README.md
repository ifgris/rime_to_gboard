# UserdbTxtToGboardZip

## 简介

本脚本可将 Rime `xxx.userdb.txt` (测试于 [Weasel](https://github.com/rime/weasel)) 转换为 Gboard `PersonalDictionary.zip` 格式, 便于将词库导入 gboard.

## 脚本依赖

- Python 3.10.9
- OpenCC 1.1.1
- tqdm 4.64.1

## 使用方法

1. 安装 python 以及依赖:

    ```
    pip install -r requirements.txt
    ```

2. 运行脚本, 按照提示将你的待转换的 `userdb.txt` 拖拽入命令行.

3. 回车, 等待数秒, `.zip` 压缩文件将自动生成.

4. 将 `.zip` 压缩文件导入手机存储中, 在 gboard 设置 - 字典 - 个人字典 - 中文 (简体) - 点击右上角 *导入* - 选择 `.zip` 压缩文件