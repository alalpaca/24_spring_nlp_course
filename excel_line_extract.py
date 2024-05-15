# 测试excel列元素提取

import pandas as pd

def excel_extract():
    # 读取Excel文件
    file_path = "pro_com_dataset.xlsx"
    output_file_path = "comments_reptile.txt"
    column_name = "Column2"
    data = pd.read_excel(file_path)

    column_data = data[column_name]

    # 写入txt文件
    with open(output_file_path, "w", encoding="utf-8") as f:
        for idx, item in enumerate(column_data):
            if isinstance(item, str):
                item = item.replace("\n", " ")
                f.write("%s\n" % item)
            else:
                print("警告：跳过非字符串行，数据集第{}行: {}".format(idx, item))

    print("评论列数据已保存至：", output_file_path)

