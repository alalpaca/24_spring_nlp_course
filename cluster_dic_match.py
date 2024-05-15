# 使用词典匹配商品各属性
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体

# 输入文件路径
input_file_path = "cluster_without_empty.txt"
output_filepath = "cluster_key_words.txt"

# 初始化存储匹配内容的字典
matches = {
    "运行速度": [],
    "屏幕效果": [],
    "散热性能": [],
    "外形外观": [],
    "轻薄程度": [],
    "物流": [],
    # 添加更多的匹配项，如需要的话
}

# 逐行读取文本文件，并进行匹配
with open(input_file_path, "r", encoding="utf-8") as input_file:
    for line in input_file:
        line = line.strip()  # 去除首尾空白字符
        for key in matches.keys():
            index = line.find(key)
            if index != -1:
                # 找到匹配项后，将匹配后的内容存储在对应的列表中
                value = line[index + len(key):].strip()  # 去除“key”后面的空白字符
                matches[key].append(value)

with open(output_filepath, "w", encoding="utf-8") as f:
    # 输出匹配结果
    for key, values in matches.items():
        print("{}: {}".format(key, values))
        f.write("{}".format(key))
        f.write("{}\n".format(values))


# 用户输入属性
input_attribute = input("请输入属性名称（例如：运行速度、屏幕效果、散热性能、外形外观、轻薄程度）：")

# 根据用户输入的属性名称生成词云图
if input_attribute in matches.keys():
    values = matches[input_attribute]  # 获取用户输入属性的匹配内容
    # 生成词云图
    text = " ".join(values)  # 将匹配的内容合并为一个字符串
    wordcloud = WordCloud(font_path='msyh.ttc', width=800, height=400, background_color="white").generate(text)
    # 显示词云图
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title(input_attribute)  # 设置标题为用户输入的属性
    plt.axis("off")
    plt.show()
else:
    print("找不到对应的属性名称，请重新输入。")