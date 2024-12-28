import pyperclip
import time

def monitor_clipboard():
    """
    监控剪切板内容变化的生成器函数。
    
    此函数会无限循环，每秒检查一次剪切板内容。
    当剪切板内容发生变化时，生成器会返回新的剪切板内容。
    """
    previous_content = ""
    while True:
        current_content = pyperclip.paste()
        if current_content != previous_content:
            previous_content = current_content
            yield current_content
        time.sleep(0.1)  # 每0.1秒检查一次剪切板

# 使用示例
# for new_clipboard_content in monitor_clipboard():
#     print(f"剪切板内容已更改: {new_clipboard_content}")