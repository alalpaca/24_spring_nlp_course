# 测试excel列元素提取

import pandas as pd

# 读取Excel文件
file_path = "pro_com_dataset.xlsx"
output_file_path = "comments_reptile.txt"
column_name = "Column2"
data = pd.read_excel(file_path)

# 提取列内容
column_data = data[column_name]

# 连接每一行的数据，并写入txt文件
with open(output_file_path, "w", encoding="utf-8") as f:
    for idx, item in enumerate(column_data):
        # 如果数据是字符串类型，将换行符替换为空格，然后写入文件
        if isinstance(item, str):
            item = item.replace("\n", " ")
            f.write("%s\n" % item)
        else:
            print("警告：跳过非字符串行，数据集第{}行: {}".format(idx, item))

print("评论列数据已保存至：", output_file_path)

