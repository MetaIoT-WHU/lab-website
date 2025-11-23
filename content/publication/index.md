---
title: Publication
nav:
  order: 1
  tooltip: Published works
header_dark: true

intro:
  title: "Selected Publications"
  icon: "fa-solid fa-microscope"
  # 原版这里有 h6，我们支持 markdown h6 写法
  content: >
    ###### (underlined authors are students in our lab)

sections:
  # --- Highlighted (不分组，直接列表) ---
  - title: "Highlighted"
    source: "data"
    data: "citations"
    key: "highlight"
    value: true
    component: "citation"
    style: "rich"
    # groupByYear: false (默认)

  # --- All Publications (开启年份分组) ---
  - title: "All"
    source: "data"
    data: "citations"
    component: "citation"
    style: "rich"
    
    # [核心修改] 开启年份分组
    groupByYear: true
    
    features:
      search: true
      filters:
        - name: "Journal"
          key: "type"
          value: "journal"
        - name: "Conference"
          key: "type"
          value: "conference"
---