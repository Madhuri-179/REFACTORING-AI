from fastapi import FastAPI, UploadFile
from services.refactoring_engine import refactor_code
from services.code_analysis import analyze_code

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile):
    code = await file.read()
    analysis = analyze_code(code.decode("utf-8"))
    return {"analysis": analysis}

@app.post("/refactor")
async def refactor(file: UploadFile):
    code = await file.read()
    refactored_code = refactor_code(code.decode("utf-8"))
    return {"refactored_code": refactored_code}
