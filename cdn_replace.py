import os
import re
import sys

# 1. 配置 CDN 域名 (去掉末尾斜杠)
CDN_DOMAIN = os.getenv("CDN_URL", "https://fast-cdn.metaiot.group/metaiot").rstrip('/')
PUBLIC_DIR = "./public"

# 2. 需要加速的目录 (不要包含 scss 或 css，防止误伤)
TARGET_FOLDERS = ["images", "files"]

def replace_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for folder in TARGET_FOLDERS:
            # ---------------------------------------------------------
            # 模式 A: 标准 HTML 属性 (src, href, data-src, srcset)
            # ---------------------------------------------------------
            # 关键改进: ([^"'\s>]+) 
            # 意思是不匹配引号、空格或右尖括号。这防止了跨标签匹配。
            # ---------------------------------------------------------
            pattern_attr = f'(src|href|srcset|data-src)=([\"\']?)(?!http|//)([^"\'\s>]+?/?){folder}/'
            
            def replace_attr(match):
                attr = match.group(1)   # src
                quote = match.group(2)  # " 或 ' 或 空
                path = match.group(3)   # 捕获到的路径，用来检查是否包含非法字符
                
                # 双重保险：如果捕获的内容太长(超过200字符)或包含 < >，说明匹配错了，不替换
                if len(path) > 200 or '<' in path or '>' in path:
                    return match.group(0)

                # 替换逻辑
                return f'{attr}={quote}{CDN_DOMAIN}/{folder}/'

            content = re.sub(pattern_attr, replace_attr, content)

            # ---------------------------------------------------------
            # 模式 B: CSS 内联样式 url(...) 
            # 解决 style="--image:url('/images/background.webp')"
            # ---------------------------------------------------------
            # 匹配 url(  --> 可选引号 --> 非http内容 --> folder --> /
            pattern_css = f'url\(([\"\']?)(?!http|//)([^"\'\)]+?/?){folder}/'
            
            def replace_css(match):
                quote = match.group(1) # " 或 ' 或 空
                # 拼接 CDN 链接
                return f'url({quote}{CDN_DOMAIN}/{folder}/'
            
            content = re.sub(pattern_css, replace_css, content)

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Replaced in: {file_path}")
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

def main():
    print(f"🚀 Starting CDN replacement... Target: {CDN_DOMAIN}")
    count = 0
    for root, dirs, files in os.walk(PUBLIC_DIR):
        for file in files:
            if file.endswith(".html"):
                replace_in_file(os.path.join(root, file))
                count += 1
    print(f"✨ Scanned {count} HTML files.")

if __name__ == "__main__":
    main()