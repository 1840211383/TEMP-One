import tkinter as tk
from tkinter import ttk
import json

class JsonGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON生成器")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 标题
        title_label = ttk.Label(main_frame, text="JSON生成器", font=("微软雅黑", 16, "bold"))
        title_label.pack(pady=10)
        
        # 字段列表
        self.fields = []
        
        # 字段输入区域
        fields_frame = ttk.LabelFrame(main_frame, text="字段设置", padding="10")
        fields_frame.pack(fill=tk.X, pady=10)
        
        # 添加字段按钮
        add_field_btn = ttk.Button(fields_frame, text="添加字段", command=self.add_field)
        add_field_btn.pack(side=tk.TOP, pady=5)
        
        # 字段容器
        self.fields_container = ttk.Frame(fields_frame)
        self.fields_container.pack(fill=tk.X, pady=5)
        
        # 生成JSON区域
        json_frame = ttk.LabelFrame(main_frame, text="生成的JSON", padding="10")
        json_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # JSON文本框
        self.json_text = tk.Text(json_frame, height=10, wrap=tk.WORD)
        self.json_text.pack(fill=tk.BOTH, expand=True)
        
        # 按钮区域
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=10)
        
        # 生成按钮
        generate_btn = ttk.Button(buttons_frame, text="生成JSON", command=self.generate_json)
        generate_btn.pack(side=tk.LEFT, padx=5)
        
        # 复制按钮
        copy_btn = ttk.Button(buttons_frame, text="复制JSON", command=self.copy_json)
        copy_btn.pack(side=tk.LEFT, padx=5)
        
        # 清除按钮
        clear_btn = ttk.Button(buttons_frame, text="清除所有", command=self.clear_all)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # 添加默认字段
        self.add_field()
    
    def add_field(self):
        """添加一个新的字段输入行"""
        field_frame = ttk.Frame(self.fields_container)
        field_frame.pack(fill=tk.X, pady=5)
        
        # 字段名输入
        field_name_label = ttk.Label(field_frame, text="字段名:")
        field_name_label.pack(side=tk.LEFT, padx=5)
        
        field_name_entry = ttk.Entry(field_frame, width=20)
        field_name_entry.pack(side=tk.LEFT, padx=5)
        
        # 字段值输入
        field_value_label = ttk.Label(field_frame, text="值:")
        field_value_label.pack(side=tk.LEFT, padx=5)
        
        field_value_entry = ttk.Entry(field_frame, width=30)
        field_value_entry.pack(side=tk.LEFT, padx=5)
        
        # 删除按钮
        delete_btn = ttk.Button(field_frame, text="删除", command=lambda: self.delete_field(field_frame))
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        # 保存字段信息
        self.fields.append((field_name_entry, field_value_entry, field_frame))
    
    def delete_field(self, field_frame):
        """删除一个字段输入行"""
        for i, (_, _, frame) in enumerate(self.fields):
            if frame == field_frame:
                self.fields.pop(i)
                field_frame.destroy()
                break
    
    def generate_json(self):
        """生成JSON并显示"""
        json_data = {}
        
        for field_name_entry, field_value_entry, _ in self.fields:
            field_name = field_name_entry.get().strip()
            field_value = field_value_entry.get().strip()
            
            if field_name:
                json_data[field_name] = field_value
        
        # 生成格式化的JSON
        formatted_json = json.dumps(json_data, ensure_ascii=False, indent=4)
        
        # 清空文本框并显示JSON
        self.json_text.delete(1.0, tk.END)
        self.json_text.insert(tk.END, formatted_json)
    
    def copy_json(self):
        """复制生成的JSON到剪贴板"""
        json_content = self.json_text.get(1.0, tk.END).strip()
        if json_content:
            self.root.clipboard_clear()
            self.root.clipboard_append(json_content)
            # 显示复制成功提示
            self.show_message("复制成功！")
    
    def clear_all(self):
        """清除所有字段和JSON"""
        # 清除所有字段
        for _, _, field_frame in self.fields:
            field_frame.destroy()
        self.fields = []
        
        # 清空JSON文本框
        self.json_text.delete(1.0, tk.END)
        
        # 添加一个新的空字段
        self.add_field()
    
    def show_message(self, message):
        """显示消息提示"""
        # 创建临时消息窗口
        msg_window = tk.Toplevel(self.root)
        msg_window.title("提示")
        msg_window.geometry("200x100")
        msg_window.transient(self.root)
        msg_window.grab_set()
        
        # 消息标签
        msg_label = ttk.Label(msg_window, text=message)
        msg_label.pack(pady=20)
        
        # 确定按钮
        ok_btn = ttk.Button(msg_window, text="确定", command=msg_window.destroy)
        ok_btn.pack()
        
        # 自动关闭
        self.root.after(2000, msg_window.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = JsonGenerator(root)
    root.mainloop()