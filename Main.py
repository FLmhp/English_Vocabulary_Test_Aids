import tkinter as tk
from tkinter import ttk, messagebox
from SearchAnswer import get_answer_from_question
from ReadClipboard import monitor_clipboard
from Extract import extract_title_and_questions, write_questions_to_excel

class QuestionAnswerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("英语词汇测试辅助工具v2.0")
        
        # 设置窗口大小
        window_width = 500
        window_height = 400
        
        # 获取屏幕宽度和高度
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # 计算窗口居中的位置
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # 设置窗口位置和大小
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # 创建按钮
        self.process_button = ttk.Button(root, text="我已将测试页面复制到剪切板", command=self.process_clipboard)
        self.process_button.pack(expand=True)
    
    def process_clipboard(self):
        try:
            new_clipboard_content = next(monitor_clipboard())
            title, questions = extract_title_and_questions(new_clipboard_content)
            write_questions_to_excel(title, questions)
            messagebox.showinfo("成功", "题目信息已保存到 Excel 文件")
        except StopIteration:
            messagebox.showerror("错误", "无法读取剪切板内容")
        except Exception as e:
            messagebox.showerror("错误", f"处理过程中发生错误: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuestionAnswerApp(root)
    root.mainloop()