
def classify_input(state):
    text = state["input"]
    if "BMI" in text or "身高" in text:
        return {"route": "BMI", "input": text}
    elif any(x in text for x in ["头痛", "乏力", "症状", "不舒服"]):
        return {"route": "Advice", "input": text}
    elif any(x in text for x in ["糖尿病", "高血糖", "血脂"]):
        return {"route": "RAG", "input": text}
    else:
        return {"route": "Exit", "input": text}
