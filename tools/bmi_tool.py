
from langchain.tools import tool

@tool
def calculate_bmi(input: str) -> str:
    try:
        height, weight = map(float, input.split(","))
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "偏瘦"
        elif bmi < 24:
            category = "正常"
        elif bmi < 28:
            category = "超重"
        else:
            category = "肥胖"
        return f"BMI={bmi:.2f}，属于{category}"
    except:
        return "输入格式有误，请输入如 1.75,65"
