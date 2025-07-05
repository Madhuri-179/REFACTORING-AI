import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load AI Model (CodeBERT)
model = AutoModelForSequenceClassification.from_pretrained("microsoft/codebert-base")
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")

def detect_tech_debt(code: str) -> str:
    inputs = tokenizer(code, return_tensors="pt")
    outputs = model(**inputs)
    
    # AI Prediction (Simplified)
    score = torch.sigmoid(outputs.logits).item()
    
    if score > 0.7:
        return "High tech debt: Needs urgent refactoring."
    elif score > 0.4:
        return "Moderate tech debt: Consider refactoring."
    else:
        return "Low tech debt: Code is up to date."
