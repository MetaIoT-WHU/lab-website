# cdn_replace.py
import os
import re
import sys

# 从环境变量获取 CDN 地址，去除末尾斜杠
CDN_DOMAIN = os.getenv("CDN_URL", "https://fast-cdn.metaiot.group").rstrip('/')
PUBLIC_DIR = "./public"

# 需要加速的文件夹
TARGET_FOLDERS = ["images", "files"]

def replace_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for folder in TARGET_FOLDERS:
            # --- V3 正则核心修改 ---
            # 1. (src|href|srcset|data-src) : 匹配常用属性
            # 2. = : 匹配等号
            # 3. ([\"\']?) : 关键修改！这里加了 ? 表示引号是可选的 (匹配 " 或 ' 或 空)
            # 4. (?!http|//) : 排除 HTTP 开头
            # 5. (.*?/?) : 匹配前缀 (如 / 或 ./)
            # 6. {folder}/ : 匹配目标文件夹
            
            pattern = f'(src|href|srcset|data-src)=([\"\']?)(?!http|//)(.*?/?){folder}/'
            
            def replace_match(match):
                attr = match.group(1)   # data-src
                quote = match.group(2)  # 引号 (可能为空)
                # prefix = match.group(3) # 原本的 /，丢弃
                
                # 拼接逻辑：保持原样的引号风格
                # 如果原来没引号，替换后也没引号 (Minify 风格)
                # 结果: data-src=https://cdn.../images/
                return f'{attr}={quote}{CDN_DOMAIN}/{folder}/'

            content = re.sub(pattern, replace_match, content)

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