import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from agent.analyzer import run_analysis
from io import StringIO


# Initialize FastAPI app
app = FastAPI(
    title="Ad Performance Analysis Agent API (Gemini Flash Edition)",
    description="An API for an AI agent that reviews ad performance CSVs and provides insights, powered by Google Gemini Flash.",
    version="3.0.0"
)


# Pydantic model for the response
class AnalysisResponse(BaseModel):
    insights: str

@app.get("/")
def read_root():
    return {"status": "Ad Analyzer Agent API (Gemini Flash Edition) is running!"}

@app.post("/analyze-ads", response_model=AnalysisResponse)
async def analyze_ads_endpoint(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")
    try:
        contents = await file.read()
        string_io = StringIO(contents.decode('utf-8'))
        df = pd.read_csv(string_io)
        required_columns = ['Impressions', 'Clicks', 'Amount Spent (USD)', 'Purchases']
        if not all(col in df.columns for col in required_columns):
            raise HTTPException(status_code=400, detail=f"CSV must contain the following columns: {required_columns}")
        insights_and_suggestions = run_analysis(df)
        return AnalysisResponse(insights=insights_and_suggestions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during analysis: {str(e)}")