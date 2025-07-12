
from langgraph_agent import app

if __name__ == "__main__":
    print("欢迎使用 LangGraph 医疗 Agent 👨‍⚕️")
    while True:
        q = input("\n请输入您的问题（输入 exit 退出）：")
        if q.lower() == "exit":
            break
        result = app.invoke({"input": q})
        print("🤖", result["result"])
