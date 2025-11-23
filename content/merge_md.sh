#!/usr/bin/env bash

# 使用方式：
#   ./merge_md.sh <源目录> <输出文件>
# 示例：
#   ./merge_md.sh ./notes merged.md

SRC_DIR="$1"
OUT_FILE="$2"

if [ -z "$SRC_DIR" ] || [ -z "$OUT_FILE" ]; then
    echo "Usage: $0 <source_dir> <output_file>"
    exit 1
fi

# 清空输出文件
> "$OUT_FILE"

# 遍历目录下所有 .md 文件
for file in "$SRC_DIR"/*.md; do
    [ -e "$file" ] || continue   # 若目录下没有 md 文件则跳过

    filename=$(basename "$file")

    echo "[$filename]" >> "$OUT_FILE"
    cat "$file" >> "$OUT_FILE"
    echo -e "\n" >> "$OUT_FILE"   # 文件之间空行
done

echo "合并完成 -> $OUT_FILE"
