import pandas as pd

def get_answer_from_question(question_text):
    # 读取Combined.xlsx文件
    combined_df = pd.read_excel('Combined.xlsx')
    
    # 查找与question_text匹配的题干
    matching_row = combined_df[combined_df['题干*'].str.contains(question_text, na=False)]
    
    # 检查是否找到匹配的题干
    if not matching_row.empty:
        # 返回对应的选项及选项内容
        option = matching_row['答案*'].values[0]
        answer = matching_row[f'选项-{option}'].values[0]
        return f'{option}.{answer}'
    else:
        return "未找到对应的题干"

# 示例用法
# question = "For the _________  geographic location, Leshan had always been a city of great financial importance for Chengdu."
# answer = get_answer_from_question(question)
# print(f"答案: {answer}")