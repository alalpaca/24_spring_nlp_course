# 情感分析
'''
from hanlp_restful import HanLPClient
HanLP = HanLPClient('https://www.hanlp.com/api', auth='NDc3MEBiYnMuaGFubHAuY29tOkdDSjJUcHBRNWp5NHU1eGY=')

input_file_path = "comments_reptile.txt"

with open(input_file_path, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
        print("情感打分:", HanLP.sentiment_analysis(line))
'''

from hanlp_restful import HanLPClient

HanLP = HanLPClient('https://www.hanlp.com/api', auth='NDc3MEBiYnMuaGFubHAuY29tOkdDSjJUcHBRNWp5NHU1eGY=')
input_file_path = "comments_reptile.txt"
output_file_path = "sentiment_scores.txt"

with open(input_file_path, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
        score = HanLP.sentiment_analysis(line)
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(str(score))
        # print("情感打分:", score)

print("情感打分已保存到", output_file_path)
