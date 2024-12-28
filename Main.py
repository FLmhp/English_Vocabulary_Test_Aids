import tkinter as tk
from tkinter import ttk
from SearchAnswer import get_answer_from_question
from ReadClipboard import monitor_clipboard

class QuestionAnswerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("英语词汇测试辅助工具v1.0")
        
        # 设置窗口大小
        window_width = 500
        window_height = 400
        
        # 获取屏幕宽度和高度
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # 计算窗口左上角的位置（右半部分居中）
        x = (screen_width // 2 + (screen_width // 2 - window_width) // 2)
        y = (screen_height - window_height) // 2
        
        # 设置窗口位置和大小
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # 创建题干标签和文本框
        self.question_label = ttk.Label(root, text="题干:")
        self.question_label.pack(pady=5)
        
        self.question_text = tk.Text(root, height=5, width=60)
        self.question_text.pack(pady=5)
        
        # 创建答案标签和文本框
        self.answer_label = ttk.Label(root, text="答案:")
        self.answer_label.pack(pady=5)
        
        self.answer_text = tk.Text(root, height=5, width=60)
        self.answer_text.pack(pady=5)
        
        # 启动剪切板监控
        self.monitor_clipboard()
    
    def monitor_clipboard(self):
        try:
            new_clipboard_content = next(monitor_clipboard())
            self.update_question_and_answer(new_clipboard_content)
        except StopIteration:
            pass
        # 每秒检查一次剪切板
        self.root.after(1000, self.monitor_clipboard)
    
    def update_question_and_answer(self, question_text):
        # 清空题干和答案文本框
        self.question_text.delete('1.0', tk.END)
        self.answer_text.delete('1.0', tk.END)
        
        # 显示新的题干
        self.question_text.insert(tk.END, question_text)
        
        # 获取答案
        answer = get_answer_from_question(question_text)
        
        # 显示答案
        self.answer_text.insert(tk.END, answer)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuestionAnswerApp(root)
    root.mainloop()