import os


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

    print(f"\n已完成 {len(hot_files)} 个")


count_hot_files()
