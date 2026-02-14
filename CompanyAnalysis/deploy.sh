#!/bin/bash

# 1. Add all changes
git add .

# 2. Commit with a timestamp
git commit -m "Update site content: $(date '+%Y-%m-%d %H:%M:%S')"

# 3. Push to GitHub main branch
git push origin main

echo "✅ 部署完成！请等待 1-2 分钟刷新 GitHub Pages 页面。"
