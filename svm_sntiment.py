from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd

# 读取标记好的数据集
data = pd.read_csv("train.tsv", sep="\t", header=None, skiprows=1, names=["Label", "Comment"])

# 划分特征和标签
X = data["Comment"]
y = data["Label"]

# 将文本特征转换为TF-IDF向量
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# 训练SVM模型
svm_model = SVC(kernel="linear")
svm_model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = svm_model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print("模型在测试集上的准确率:", accuracy)

# 在最终的数据集上进行情感分类
final_data = pd.read_csv("comments_reptile.txt", sep="\t", header=None, names=["Comment"])
final_X_tfidf = tfidf_vectorizer.transform(final_data["Comment"])
final_y_pred = svm_model.predict(final_X_tfidf)

# 将情感分类结果写入文件
with open("sentiment_scores.txt", "w", encoding="utf-8") as f:
    for comment, sentiment in zip(final_data["Comment"], final_y_pred):
        f.write(f"{sentiment}\n")

print("情感分类结果已保存到 sentiment_results.txt 文件。")