

import os
import time

def list_files_simple():
    """简单版本 - 只列出文件，逗号分隔"""
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files.sort()
    
    # 一行显示所有文件
    print(", ".join(files))
    
    # 保持打开以便复制
    print(f"\n共 {len(files)} 个文件")
    print("按 Ctrl+C 复制内容后，关闭窗口或等待30秒...")
    
    try:
        time.sleep(30)
    except KeyboardInterrupt:
        print("\n用户中断，程序结束")

if __name__ == "__main__":
    list_files_simple()