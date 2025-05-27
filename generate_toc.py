import os
import re
import shutil

def generate_toc(readme_path, output_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    chapters = re.findall(r'### (第\d+章：.*?)(?=### 第\d+章：|\Z)', content, re.DOTALL)
    toc = "## 文档目录\n\n"
    
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    vue_template = os.path.join(template_dir, "demo.vue")
    os.makedirs(template_dir, exist_ok=True)

    if not os.path.exists(vue_template):
        with open(vue_template, 'w', encoding='utf-8') as f:
            f.write('<template>\n  <div>\n    <!-- 示例组件 -->\n  </div>\n</template>\n\n<script>\nexport default {\n  name: "DemoComponent"\n}\n</script>')

    for chapter in chapters:
        title = chapter.split('\n')[0].strip()
        chapter_num = re.search(r'第(\d+)章', title).group(1)
        
        # 提取章节下所有小节链接
        section_links = re.findall(r'\[\* (.*?)\]\((.*?)\)', chapter)
        for section_name, section_path in section_links:
            dir_path = section_path.split('/README.md')[0]
            os.makedirs(dir_path, exist_ok=True)
            
            existing_files = os.listdir(dir_path) if os.path.exists(dir_path) else []
            has_readme = "README.md" in existing_files
            has_demo = "demo.vue" in existing_files
            
            if not has_readme:
                with open(os.path.join(dir_path, "README.md"), 'w', encoding='utf-8') as f:
                    f.write(f"# {section_name}\n\n本节内容待补充...")
            
            if not has_demo:
                shutil.copy(vue_template, dir_path)
        
        toc += f"* [{title}](./examples/{chapter_num.zfill(2)}/{chapter_num.zfill(2)}01/README.md)\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(toc)
    
    print(f"目录已生成到 {output_path}")

if __name__ == "__main__":
    readme_path = "/Users/yuanjing/Desktop/Vue3-doc/README.md"
    output_path = "/Users/yuanjing/Desktop/Vue3-doc/TOC.md"
    generate_toc(readme_path, output_path)