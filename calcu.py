import os

import os


def count_lines(file_path):
    """
    工具函数：计算文件行数
    逻辑行数 > 5
    """
    line_count = 0
    try:
        # 使用 utf-8 编码读取，忽略可能的编码错误
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for _ in f:
                line_count += 1
    except Exception as e:
        print(f"无法读取文件 {file_path}: {e}")
        return 0
    return line_count


def count_hot_files_with_min_lines(min_lines=5):
    # 获取当前执行目录
    current_dir = os.getcwd()
    # 列出所有文件
    files = os.listdir(current_dir)

    valid_hot_files = []

    for f in files:
        file_path = os.path.join(current_dir, f)

        # 条件 1: 以 'hot_' 开头
        # 条件 2: 是文件而不是文件夹
        if f.startswith("hot_") and os.path.isfile(file_path):
            # 条件 3: 代码行数 > min_lines
            if count_lines(file_path) < min_lines:
                valid_hot_files.append(f)

    print(f"TODO: {len(valid_hot_files)} 个")
    print(f"TODO: {valid_hot_files}")


def count_hot_files():
    # 获取当前执行目录
    current_dir = os.getcwd()
    # 列出所有文件
    files = os.listdir(current_dir)

    # 过滤出以 'hot_' 开头且是文件的项
    # os.path.isfile 确保不会把名为 'hot_xxx' 的文件夹也算进去
    hot_files = [
        f
        for f in files
        if f.startswith("hot_") and os.path.isfile(os.path.join(current_dir, f))
    ]

    print(f"\n目前总计: {len(hot_files)} 个")


count_hot_files()
count_hot_files_with_min_lines(5)
