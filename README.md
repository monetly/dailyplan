# 🌟 dailyplan

> 🗓️ 一个简单的 CLI 工具，用于 **生成每日任务 iCalendar 文件** (输出 `.ics` 可导入日历)。  

📂 GitHub 仓库：[**monetly/dailyplan**](https://github.com/monetly/dailyplan)

---

## 🚀 安装

```bash
git clone https://github.com/monetly/dailyplan.git
cd dailyplan
pip install -e .
```

---

## 📝 配置文件

仓库中提供了一个示例模板：`src/dailyplan/config/tasks.yaml`  

示例内容如下（请根据需要修改）：  

```yaml
tasks:
  - title: 文献调研与笔记
    desc: 收集并阅读相关领域的核心论文，做笔记并整理参考文献。  

  - title: 论文大纲设计
    desc: 根据研究主题，拟定论文框架与章节逻辑，确定主要研究问题和贡献点。  

  - title: 数据与实验整理
    desc: 汇总已有实验结果，或进行补充实验，并清理数据以便后续撰写。  

  - title: 初稿撰写
    desc: 按照大纲完成初稿，重点保证逻辑完整性，而非文字润色。  

  - title: 修改与润色
    desc: 根据导师/合作者反馈，修改逻辑漏洞，润色语言，优化图表。  

  - title: 投递与准备答复
    desc: 准备 Cover Letter，检查格式要求，提交论文，并预演可能的审稿意见答复。  
```

请复制示例为 `src/dailyplan/config/tasks.yaml` 或在仓库根目录创建 `tasks.yaml` 并按格式填写。

---

## 💻 用法

查看帮助：

```bash
myplan -h
```

输出：

```less
usage: myplan [-h] --start START [--tasks TASKS] [--outfile OUTFILE] [--hour HOUR] [--duration DURATION]

生成每日任务 iCalendar 文件

options:
  -h, --help           show this help message and exit
  --start START        起始日期 (格式: YYYYMMDD)
  --tasks TASKS        任务文件 (默认: config/tasks.yaml)
  --outfile OUTFILE    输出文件名 (默认: plan.ics)
  --hour HOUR          每天开始的小时 (24小时制, 默认 8 点)
  --duration DURATION  任务持续小时数 (默认 3 小时)
```

---

## 🎯 示例

- 使用默认配置，生成 `plan.ics`：  
```bash
myplan --start 20251001
```

- 使用自定义任务文件、输出名、开始时间和持续时间：  
```bash
myplan --start 20251001 --tasks src/config/tasks.yaml --outfile myplan.ics --hour 9 --duration 2
```

生成的 `.ics` 文件可直接导入 **Google 日历 / iCloud / Outlook** 等。

---
