import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser

from config.config import settings

def run_analysis(df: pd.DataFrame):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-latest",
        temperature=0,
        google_api_key=settings.GOOGLE_API_KEY,
        convert_system_message_to_human=True 
    )
    pandas_agent_executor = create_pandas_dataframe_agent(
        llm=llm,
        df=df,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True,
        handle_parsing_errors=True,
        allow_dangerous_code=True
    )
    analysis_prompt = """
    First, calculate the following key performance indicators (KPIs) for each ad:
    1. Click-Through Rate (CTR) = Clicks / Impressions
    2. Cost Per Click (CPC) = Amount Spent (USD) / Clicks
    3. Conversion Rate (CR) = Purchases / Clicks
    4. Cost Per Acquisition (CPA) = Amount Spent (USD) / Purchases
    After calculating the KPIs, please provide a summary that answers these questions:
    - Which ad is the top performer based on CPA and CTR?
    - Which ad is the worst performer based on CPA and CTR?
    - Are there any campaigns (Ad Set Name) that are significantly outperforming others?
    Present the final summary in a clear, bulleted list.
    """
    print("---EXECUTING PANDAS AGENT (GEMINI FLASH) FOR QUANTITATIVE ANALYSIS---")
    quantitative_summary = pandas_agent_executor.invoke({"input": analysis_prompt})['output']
    synthesis_prompt = ChatPromptTemplate.from_template(
        """
        You are a world-class Senior Marketing Strategist. You have been given a data-driven summary of an ad campaign's performance.
        Your task is to provide actionable insights and creative improvement suggestions.
        **Performance Summary:**
        {summary}
        **Your Tasks:**
        1.  Top Performer Analysis: Based on the top-performing ad(s), what hypotheses can you form about why they succeeded?
        2.  Underperformer Diagnosis: For the worst-performing ad(s), what are the likely reasons for their failure?
        3.  Actionable Creative Suggestions: Provide 3-5 concrete, creative suggestions to improve the underperforming ads or to create new ads based on the learnings from the top performers.
        Provide your response in a well-structured markdown format.
        """
    )
    synthesis_chain = synthesis_prompt | llm | StrOutputParser()
    print("\n---SYNTHESIZING INSIGHTS AND SUGGESTIONS (GEMINI FLASH)---")
    final_insights = synthesis_chain.invoke({"summary": quantitative_summary})
    return final_insights