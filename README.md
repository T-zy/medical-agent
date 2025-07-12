
# Medical LangChain Agent

这是一个医疗问答智能助手，基于 LangChain Agent 构建，支持以下功能：

- 📄 医学知识问答（RAG）
- 🧮 BMI 指数计算
- 📋 根据症状提供初步就诊建议

## 快速开始

```bash
git clone ...
cd medical-agent
pip install -r requirements.txt
```

设置 `.env` 文件：

```
OPENAI_API_KEY=你的KEY
```

运行：

```bash
python main.py
```

## 示例问法

- 我的身高是1.75米，体重是70公斤，BMI是多少？
- 我最近总是头痛，怎么办？
- 糖尿病患者需要监测哪些指标？


---

## 🚀 LangGraph 医疗智能 Agent 工作流图

```mermaid
graph TD;
    用户输入 --> 分类节点;
    分类节点 -->|包含 BMI| BMI工具;
    分类节点 -->|包含 头痛/症状| 建议工具;
    分类节点 -->|包含 糖尿病/高血糖| RAG工具;
    分类节点 -->|其他| 退出节点;
    BMI工具 --> 结束;
    建议工具 --> 结束;
    RAG工具 --> 结束;
    退出节点 --> 结束;
```

---

## ☁️ Git 使用（推送至你的仓库）

```bash
cd medical-agent
git init
git remote add origin https://github.com/T-zy/medical-agent.git
git add .
git commit -m "initial commit: LangGraph medical agent"
git branch -M main
git push -u origin main
```

---
