import re
import jieba
def load_sentiment_dictionary(file_path):
    """
    从文件中加载情感词典，并返回一个字典，键为词汇，值为情感得分。
    """
    sentiment_dict = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                match = re.match(r"(.+?)\s+([-+]?\d*\.?\d+)", line)
                if match:
                    word = match.group(1)
                    score = float(match.group(2))
                    sentiment_dict[word] = score
                else:
                    print(f"警告：跳过格式不正确的行：{line}")
    return sentiment_dict

def calculate_sentiment_score(text, sentiment_dict):
    """
    计算文本的情感得分，基于情感词典。
    """
    words = jieba.lcut(text)
    print(words)
    sentiment_score = 0
    for word in words:
        if word in sentiment_dict:
            sentiment_score += sentiment_dict[word]
    return sentiment_score

# 加载情感词典
sentiment_dict = load_sentiment_dictionary("sentiment_dictionary.txt")  # 替换为你的情感词典文件路径

# 计算文本的情感得分
text = "2023年生产这个翘口比买一个iPad划算很多，值得好好体验"
sentiment_score = calculate_sentiment_score(text, sentiment_dict)
print("文本的情感得分:", sentiment_score)
