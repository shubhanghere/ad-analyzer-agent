# Ad Performance Analysis Agent

## Project Overview

This is an AI-powered ad analysis tool that reads marketing performance data from a CSV file and generates a full report. The agent identifies key performance metrics like CTR and CPA, highlights the best and worst performing ads, and provides creative suggestions to improve your campaigns.

The project uses:
- **Python** for backend logic
- **LangChain** to manage agent behavior
- **Google’s Gemini Flash Model** for AI analysis
- **FastAPI** to serve the application through a web API

---

## How It Works

The agent follows a two-step analysis process:

### 1. Quantitative Analysis
It uses Pandas to read and analyze the uploaded CSV file. In this step, it calculates all the important KPIs like:
- Click-Through Rate (CTR)
- Cost Per Acquisition (CPA)
- Conversion Rate
- ROAS (Return on Ad Spend)

---


### 2. Qualitative Synthesis
The AI then interprets this data like a human strategist. It explains:
- Why certain ads worked well or failed
- What trends it noticed
- What improvements or new ideas you could try

---

## How to Use the Agent

You can either use the **live deployed version** or run the app **locally on your machine**.

---

## Option 1: Try It Online (Live Demo)

### Step 1: Open the App-:

Visit the live app at:
https://ad-analyzer-agent.onrender.com/docs


Note: (If it takes a few seconds to load, it's just the free server waking up.)



---

### Step 2: Upload and Analyze a File

1. Scroll to the `POST /analyze-ads` section.
2. Click **Try it out**.
3. Click **Choose File** and upload your CSV (use `sample_meta_ads.csv` from the `data/` folder).
4. Click the **Execute** button.
5. Wait for a few seconds to see the full analysis in the "Server response" section.

---

## Option 2: Run It on Your Local Machine

## Steps
Open a terminal and run:
 ---uvicorn main:app
 make sure to actiavte the venv and install the requirements.txt file.


