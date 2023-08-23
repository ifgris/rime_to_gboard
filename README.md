# rime_to_gboard

## 简介

借助 Rime 输入法的 `userdb.txt` 用户词库, 让 Gboard 的输入体验媲美旧时的 Google Pinyin.

本脚本可将 Rime `xxx.userdb.txt` (测试于 [Weasel](https://github.com/rime/weasel)) 转换为 Gboard `PersonalDictionary.zip` 格式, 便于将词库导入 Gboard.

## 适用输入方案

- 全拼
- 五笔 (测试)

## 脚本依赖

- Python 3.8-3.10
  - OpenCC 1.1.1
  - tqdm 4.64.1

## 使用方法

### 命令行启动

1. 安装 python 以及依赖:

    ```shell
    pip install -r requirements.txt
    ```

2. 运行脚本, 按照提示将你的待转换的 `userdb.txt` 拖拽入命令行, 或输入文件路径.

3. 根据指引, 确认输入方案, 输入文件文本繁简类型.

4. 回车, 等待数秒, `.zip` 压缩文件将自动生成.

5. 将 `.zip` 压缩文件导入手机存储中, 在 Gboard 设置 - 字典 - 个人字典 - 中文 (简体) - 点击右上角 *导入* - 选择 `.zip` 压缩文件.

### 使用应用程序

1. [下载](https://github.com/cgcel/rime_to_gboard/releases) 应用程序, 保存至本地
2. 打开 rime2gboard.exe, 按照提示将待转换的 `*.userdb.txt` 拖入窗口, 或直接输入文件路径
3. 按照后续提示确认输入方案, 输入繁简类型后回车
4. 与 [上述](#命令行) 第5步操作一致

## License

```License
Copyright 2023 GC Chen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
