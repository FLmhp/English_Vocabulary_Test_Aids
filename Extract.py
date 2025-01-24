import re
import pandas as pd
from SearchAnswer import get_answer_from_question

def extract_title_and_questions(text):
    # 提取测试标题
    text = text.replace("\u200f", "").replace("\u200e", "").replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
    # text = re.sub(r'\n+', lambda m: '\n' * (len(m.group(0)) - 1), text) 
    text = text.replace("\r", "")
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'\n\n(\d)', r'\n\1', text)
    title_match = re.search(r'新版考试\n(.*?)\n', text)
    title = title_match.group(1).strip() if title_match else "未找到标题"

    # 提取题目和选项
    questions = re.findall(r'\d\.单选\(2分\)\n([A-Z].*?)\n.*?\n[A-Z]\.\n(.*?)\n[A-Z]\.\n(.*?)\n[A-Z]\.\n(.*?)\n[A-Z]\.\n(.*?)\n', text, re.DOTALL)

    # 对每个元素执行 strip()
    questions = [(q[0].strip(), *[opt.strip() for opt in q[1:]]) for q in questions]

    return title, questions

def write_questions_to_excel(title, questions):
    # 创建一个 DataFrame 来存储题目信息
    data = []
    for question, option_a, option_b, option_c, option_d in questions:
        options = dict(zip(['A', 'B', 'C', 'D'], [option_a, option_b, option_c, option_d]))
        data.append({
            '题干': question,
            '答案': get_answer_from_question(question, **options),
            '选项-A': option_a,
            '选项-B': option_b,
            '选项-C': option_c,
            '选项-D': option_d
        })
    
    df = pd.DataFrame(data)
    
    # 将 DataFrame 写入 Excel 文件
    file_name = f"{title}.xlsx"
    df.to_excel(file_name, index=False)
    print(f"题目信息已保存到 {file_name}")

# # 从文件中读取文本内容
# # with open('Copy.txt', 'r', encoding='utf-8') as file:
# with open('2.txt', 'r', encoding='utf-8') as file:
#     text = file.read()

# # 调用函数提取题目和选项
# title, questions = extract_title_and_questions(text)

# # 将题目信息写入 Excel 文件
# write_questions_to_excel(title, questions)