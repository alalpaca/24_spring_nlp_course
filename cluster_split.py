# 文本处理 - 指定商品导出为txt文件，包含对应所有评论，已分句
import pandas as pd

# 读取 Excel 文件
excel_file = "pro_com_dataset.xlsx"  # 请替换为你的 Excel 文件路径
df = pd.read_excel(excel_file)

# 用户输入商品名称
product_name = input("请输入商品名称：")

# 根据商品名称筛选数据
filtered_data = df[df['Column1'] == product_name]

# 输出到文本文件
output_file_path = "cluster_test.txt"
with open(output_file_path, "w", encoding="utf-8") as f:
    # f.write("商品名称: {}\n".format(product_name))
    # f.write("相符的内容:\n")
    for index, row in filtered_data.iterrows():
        column2_value = str(row['Column2'])
        column2_value = column2_value.replace("【评论】", "")
        # column2_value = column2_value.replace("\n", "")
        column2_value = column2_value.replace("！！！！！", "!")
        column2_value = column2_value.replace("！！！", "!")
        column2_value = column2_value.replace("！", ",")
        column2_value = column2_value.replace("，", "\n")
        column2_value = column2_value.replace("。", "\n")
        column2_value = column2_value.replace(";", "\n")
        column2_value = column2_value.replace("？", "\n")

        # 【商品名称】商品100009464799
        f.write("{}\n".format(column2_value))

print("提取内容已保存到", output_file_path)

# 空行处理
input_file_path = "cluster_test.txt"
output_file_path = "cluster_without_empty.txt"

# 读取输入文件，并过滤掉空行
with open(input_file_path, "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]

# 将非空行写入输出文件
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for line in non_empty_lines:
        output_file.write(line + "\n")

print("空行已移除，内容已保存到", output_file_path)
