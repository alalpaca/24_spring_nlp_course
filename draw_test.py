import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体

# 读取 Excel 文件
excel_file = "sentiscore_pro.xlsx"  # 请替换为你的 Excel 文件路径
df = pd.read_excel(excel_file)

# 用户输入商品名称
product_name = input("请输入商品名称：")

# 根据商品名称筛选数据
product_data = df[df['商品名称'] == product_name]

# 统计情感分数
positive_count = (product_data['情感分数'] == 1).sum()
negative_count = (product_data['情感分数'] == 0).sum()

general_score = positive_count / (positive_count + negative_count)
print("综合好评率为：", round(general_score * 100, 2), "%")

# 输出消极和积极个数
print("商品名称：", product_name)
print("积极评论数量：", positive_count)
print("消极评论数量：", negative_count)

# 绘制饼图
labels = ['Positive', 'Negative']
sizes = [positive_count, negative_count]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # 突出显示积极评论部分

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Sentiment Analysis for {}".format(product_name))
plt.axis('equal')  # 使得饼图比例相等
plt.show()
