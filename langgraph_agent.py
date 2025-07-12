
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool
from langgraph.graph import StateGraph, END
from langchain.chains import RetrievalQA
from tools.bmi_tool import calculate_bmi
from tools.advice_tool import give_health_advice
from rag import get_medical_vectorstore
from nodes.classify_node import classify_input
from nodes.exit_node import exit_func
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(temperature=0)

vectordb = get_medical_vectorstore()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

tool_dict = {
    "BMI": calculate_bmi,
    "Advice": give_health_advice,
    "RAG": qa_chain.run
}

class AgentState(dict):
    pass

workflow = StateGraph(AgentState)

workflow.add_node("classify", classify_input)
workflow.add_node("bmi_tool", lambda state: {"result": tool_dict["BMI"](state["input"])})
workflow.add_node("advice_tool", lambda state: {"result": tool_dict["Advice"](state["input"])})
workflow.add_node("rag_tool", lambda state: {"result": tool_dict["RAG"](state["input"])})
workflow.add_node("exit", exit_func)

workflow.set_entry_point("classify")
workflow.add_conditional_edges("classify", lambda s: s["route"], {
    "BMI": "bmi_tool",
    "Advice": "advice_tool",
    "RAG": "rag_tool",
    "Exit": "exit"
})

for node in ["bmi_tool", "advice_tool", "rag_tool"]:
    workflow.add_edge(node, END)
workflow.add_edge("exit", END)

app = workflow.compile()
