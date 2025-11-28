import os
import re
import sys

# --- 配置区域 ---
# 优先读取环境变量，如果没有则使用默认值
CDN_DOMAIN = os.getenv("CDN_URL", "https://fast-cdn.metaiot.group") 
PUBLIC_DIR = "./public"
TARGET_DIRS = ["/images/", "/files/"]
# ----------------

def replace_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 遍历需要替换的目录前缀
        for target_dir in TARGET_DIRS:
            # 逻辑：
            # 1. 查找 src="/images/..." 替换为 src="CDN/images/..."
            # 2. 查找 href="/images/..." 替换为 href="CDN/images/..."
            # 注意：这里使用简单的字符串替换，这比正则更安全且足够处理 Hugo 生成的标准路径
            
            # 构造本地绝对路径引用 (Hugo 通常生成 /images/xxx)
            local_ref = f'"{target_dir}'
            # 构造 CDN 路径引用
            cdn_ref = f'"{CDN_DOMAIN}{target_dir}'
            
            content = content.replace(f'src={local_ref}', f'src={cdn_ref}')
            content = content.replace(f'href={local_ref}', f'href={cdn_ref}')
            
            # 处理 srcset (响应式图片)
            # srcset="/images/a.jpg 1x, /images/b.jpg 2x"
            content = content.replace(f'srcset={local_ref}', f'srcset={cdn_ref}')
            # srcset 中间的部分 (逗号后面的空格 + 路径)
            content = content.replace(f', {target_dir}', f', {CDN_DOMAIN}{target_dir}')

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Processed: {file_path}")
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

def main():
    print(f"🚀 Starting CDN replacement... Target: {CDN_DOMAIN}")
    
    # 遍历 public 目录下的所有 html 文件
    for root, dirs, files in os.walk(PUBLIC_DIR):
        for file in files:
            if file.endswith(".html"):
                replace_in_file(os.path.join(root, file))
                
    print("✨ CDN replacement finished!")

if __name__ == "__main__":
    print(f"🚀 Starting CDN replacement using: {CDN_DOMAIN}")
    main()