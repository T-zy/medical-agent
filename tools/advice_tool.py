
from langchain.tools import tool

@tool
def give_health_advice(symptom: str) -> str:
    if "头痛" in symptom:
        return "建议监测血压，若持续不适请就诊神经内科。"
    elif "视力模糊" in symptom:
        return "建议眼科或内分泌科检查血糖、眼底。"
    elif "乏力" in symptom:
        return "可能与营养或慢性病相关，建议查血常规、电解质。"
    else:
        return "请提供更具体的症状，以获得更好的建议。"
