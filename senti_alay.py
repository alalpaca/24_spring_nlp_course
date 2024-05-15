# 情感分析
'''
from hanlp_restful import HanLPClient

HanLP = HanLPClient('https://www.hanlp.com/api', auth='NDc3MEBiYnMuaGFubHAuY29tOkdDSjJUcHBRNWp5NHU1eGY=')
input_file_path = "comments_reptile.txt"
output_file_path = "sentiment_scores_hanlp.txt"

with open(input_file_path, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
        score = HanLP.sentiment_analysis(line)
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(str(score))
        # print("情感打分:", score)

print("情感打分已保存到", output_file_path)
'''

import time
from hanlp_restful import HanLPClient

HanLP = HanLPClient('https://www.hanlp.com/api', auth='NDc3MEBiYnMuaGFubHAuY29tOkdDSjJUcHBRNWp5NHU1eGY=')
input_file_path = "comments_reptile.txt"
output_file_path = "sentiment_scores_hanlp_test1.txt"

with open(input_file_path, "r", encoding="utf-8") as f_input, open(output_file_path, "w", encoding="utf-8") as f_output:
    lines = f_input.readlines()
    total_lines = len(lines)
    lines_per_batch = 50
    time_interval = 65  # 每批50句话之后的时间间隔，单位为秒

    for i in range(0, total_lines, lines_per_batch):
        start_time = time.time()
        for line in lines[i:i+lines_per_batch]:
            print(line.strip())
            score = HanLP.sentiment_analysis(line)
            f_output.write(str(score) + '\n')

        end_time = time.time()
        elapsed_time = end_time - start_time
        remaining_time = max(0, time_interval - elapsed_time)  # 每批执行时间，减去实际执行时间
        time.sleep(remaining_time)

print("情感打分已保存到", output_file_path)

