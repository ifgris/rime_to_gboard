# -*- coding: utf-8 -*-

from tqdm import tqdm
from hanzidentifier import is_traditional

def contains_traditional(text):
    return is_traditional(text)

def remove_traditional_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 过滤包含繁体字的行
    simplified_lines = []
    for line in tqdm(lines, desc='Processing', unit='line'):
        if not contains_traditional(line):
            simplified_lines.append(line)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(simplified_lines)

def main():
    input_file = input("输入文件名: ")  # 输入文件名
    output_file = 'output.txt'  # 输出文件名

    remove_traditional_lines(input_file, output_file)
    print(f"已从 {input_file} 中去除包含繁体字的行, 并将结果保存到 {output_file} 中.")

if __name__ == "__main__":
    main()