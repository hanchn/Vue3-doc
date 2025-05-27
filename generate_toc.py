import os
import re
import shutil

def generate_toc(readme_path, output_path):
    # 读取README.md内容
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取章节标题和内容
    chapters = re.findall(r'### (第\d+章：.*?)(?=### 第\d+章：|\Z)', content, re.DOTALL)
    
    # 生成目录
    toc = "## 文档目录\n\n"
    existing_links = set()
    
    # 模板文件路径改为绝对路径
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    vue_template = os.path.join(template_dir, "demo.vue")
    
    # 确保模板目录存在
    os.makedirs(template_dir, exist_ok=True)
    
    # 如果模板文件不存在，创建默认demo.vue
    if not os.path.exists(vue_template):
        with open(vue_template, 'w', encoding='utf-8') as f:
            f.write('<template>\n  <div>\n    <!-- 示例组件 -->\n  </div>\n</template>\n\n<script>\nexport default {\n  name: "DemoComponent"\n}\n</script>')

    for chapter in chapters:
        # 提取章节标题
        title = chapter.split('\n')[0].strip()
        chapter_num = re.search(r'第(\d+)章', title).group(1)
        
        # 创建章节目录结构
        dir_path = f"examples/{chapter_num.zfill(2)}/{chapter_num.zfill(2)}01"
        os.makedirs(dir_path, exist_ok=True)
        
        # 检查目录是否已有文件
        existing_files = os.listdir(dir_path) if os.path.exists(dir_path) else []
        
        # 检查README.md和demo.vue是否都存在
        has_readme = "README.md" in existing_files
        has_demo = "demo.vue" in existing_files
        
        # 创建README.md如果不存在
        if not has_readme:
            with open(os.path.join(dir_path, "README.md"), 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n本章内容待补充...")
        
        # 复制demo.vue模板如果不存在
        if not has_demo:
            shutil.copy(vue_template, dir_path)
            print(f"已创建demo.vue在 {dir_path}")
        
        # 添加到目录
        toc += f"* [{title}](./{dir_path}/README.md)\n"
    
    # 写入输出文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(toc)
    
    print(f"目录已生成到 {output_path}")
    if existing_links:
        print(f"已跳过以下已存在的章节: {', '.join(existing_links)}")

if __name__ == "__main__":
    readme_path = "/Users/yuanjing/Desktop/Vue3-doc/README.md"
    output_path = "/Users/yuanjing/Desktop/Vue3-doc/TOC.md"
    generate_toc(readme_path, output_path)