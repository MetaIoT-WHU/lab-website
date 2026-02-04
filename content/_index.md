---
title: "MetaIoT Lab"
header_dark: true

# 这里定义首页的“介绍”部分
intro:
  title: "MetaIoT Lab"
  background: ""
  dark: false
  content: >
    Here at Mobile, Sensing, Automative & Internet of Things Lab (MetaIoT), which is leaded by [Prof. Qian Zhang](https://www.cse.ust.hk/~qianzh/) and [Prof. Wei Wang](https://metaiot.group/weiwang.html)([学校主页](https://cs.whu.edu.cn/info/1019/55961.htm)). We create the next generation of intelligent unmanned systems for sensing and perception with applications in autonomous systems, AIoT, and embodied AI.

# 这里定义后续的“模块列表”
sections:
  - title: "Research Overview"
    content: |
      - **Spatial Perception and Intelligence for Embodied AI:** including embodied spatial intelligence, integrating perception, cognition, and action for autonomous agents in complex environments.
      - **mmWave/multi-modal 3D Perception and SLAM:** including mmWave Radar perception, multi-modal SLAM/navigation for embodied AI and self-driving vehicles.
      - **AIoT:** including AIoT hardware design and embedded systems for industry and healthcare.
    # 2. 列表数据部分
    source: "data"
    data: "projects"
    key: "group"
    value: "theme"
    component: "card"
    # style: "" (默认为空，或者根据需要设置)

# [第二个区块：Recent Research Projects]
  - title: "Recent Research Projects"
    # 这个区块没有 content，只有 list 数据，也可以正常工作
    source: "data"
    data: "projects"
    key: "group"
    value: "project"
    style: "project"
    component: "card"
---