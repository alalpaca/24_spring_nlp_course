# 测试excel列元素提取

import pandas as pd

# 读取Excel文件
file_path = "pro_com_dataset.xlsx"  # 替换为你的Excel文件路径
output_file_path = "comments_reptile.txt"
column_name = "Column2"  # 替换为你要提取的列的列名
data = pd.read_excel(file_path)

# 提取列内容
column_data = data[column_name]
print(column_data)

with open(output_file_path, "w", encoding="utf-8") as f:
    for item in column_data:
        f.write("%s\n" % item)
print()
print("评论列数据已保存至：", output_file_path)

