# Customer Retention Intelligence Using Agentic AI

A production-grade Agentic AI system that predicts customer churn, explains the reasoning using SHAP, and utilizes a multi-agent orchestrated workflow (Risk, Explainability, Strategy, Simulation, Communication) to proactively recommend and simulate business actions.

## 🌟 Features
- **Agentic AI Orchestration**: Leverages LangGraph to manage a cyclic workflow of specific AI sub-agents.
- **XGBoost Risk Assessor**: Accurately predicts churn probability based on customer profiles.
- **Explainable AI (SHAP)**: Extracts specific friction points for high-risk customers, feeding exact data points to the Strategy Agent rather than using generic assumptions.
- **Groq-Powered Reasoning Engine**: Uses the lightning-fast `llama-3.3-70b-versatile` via Groq API to formulate strategic interventions, simulate probabilistic outcomes, and draft precise customer outreach.
- **FAANG-Tier React UI**: A stunning, ultra-premium React dashboard using `Vite` and `Framer Motion` for staggered data revelation, animated pipelines, and beautiful CSS aesthetics.

## 🏗 System Architecture

The system utilizes an event-driven flow managed by `FastAPI` and `LangGraph`.

1. **Input**: A customer profile is captured by the React UI and sent to the FastAPI backend.
2. **Orchestrator**: LangGraph initializes the state and kicks off the sequence.
3. **Risk Agent**: Evaluates the probability of churn via our trained XGBoost system.
4. **Explainability Agent**: Extracts core drivers using SHAP logic.
5. **Strategy Agent**: Formulates a precise intervention policy (Groq).
6. **Simulation Agent**: Predicts the new churn probability post-intervention (Groq).
7. **Communication Agent**: Drafts a highly tailored retention message (Groq).
8. **Output**: The JSON results are rendered iteratively across the React dashboard.

## 🚀 Setup & Execution

### Prerequisites
- Python 3.9+
- Node.js (v16+)
- A Groq API Key (`gsk_...`)

### 1. Installation
```bash
# Backend Setup
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt

# Frontend Setup
cd frontend
npm install
cd ..
```

### 2. Prepare the ML Pipeline
Generates synthetic data (`telecom_churn.csv`) and fits the XGBoost models & SHAP explainers.
```bash
cd ml_pipeline
python data_generator.py
python train.py
cd ..
```

### 3. Environment Variables
Create a file named `.env` in the root folder with the following content:
```env
GROQ_API_KEY="your_api_key_here"
```

### 4. Run the Stack (Two Terminals Required)

**Terminal 1 (Backend API):**
```bash
# Windows
.\venv\Scripts\uvicorn.exe backend.api.main:app --reload

# Mac/Linux
uvicorn backend.api.main:app --reload
```

**Terminal 2 (Frontend React UI):**
```bash
cd frontend
npm run dev
```

Navigate to `http://localhost:5173/` safely connected to your `8000` backend API.

## 🚀 Deployment Guide (How to deploy to Production)

**1. Github Repository**
Always push your code to GitHub first. Create a blank repo on Github, then run:
```bash
git init
git add .
git commit -m "Final Product Release"
git branch -M main
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

**2. Deploy Backend (Render.com)**
- Create a new "Web Service" on Render and link your Github Repo.
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn backend.api.main:app --host 0.0.0.0 --port $PORT`
- *Important*: Add your `GROQ_API_KEY` in Render's Environment Variables settings!

**3. Deploy Frontend (Vercel.com)**
- Import the same GitHub repo into Vercel.
- Wait! Before deploying, you must edit `frontend/src/App.jsx` and `frontend/vite.config.js`. You need to replace `/api/v1/run-agents` in `axios.post` with the fully deployed Render URL you just got (e.g., `https://your-backend.onrender.com/api/v1/run-agents`). 
- Change the Root Directory in Vercel settings to `frontend/`.
- Deploy! Vercel will automatically run `npm run build`.
